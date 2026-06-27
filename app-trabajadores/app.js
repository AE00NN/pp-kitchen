const API_URL = 'REEMPLAZAR_CON_URL_API_GATEWAY';

const SIGUIENTE = {
  'RECIBIDO':'EN_COCINA','EN_COCINA':'EN_DESPACHO',
  'EN_DESPACHO':'EN_REPARTO','EN_REPARTO':'ENTREGADO'
};
const PILL = {
  'RECIBIDO':    '<span class="pp-pill pp-pill--recibido">RECIBIDO</span>',
  'EN_COCINA':   '<span class="pp-pill pp-pill--cocina">EN COCINA</span>',
  'EN_DESPACHO': '<span class="pp-pill pp-pill--despacho">EN DESPACHO</span>',
  'EN_REPARTO':  '<span class="pp-pill pp-pill--reparto">EN REPARTO</span>',
  'ENTREGADO':   '<span class="pp-pill pp-pill--entregado">ENTREGADO</span>',
};

async function cargarPedidos() {
  try {
    const res  = await fetch(`${API_URL}/tasks/pendientes`);
    const data = await res.json();
    renderTabla(data.tareas || []);
  } catch(e) {
    document.getElementById('filas-pedidos').innerHTML =
      '<tr><td colspan="5" style="color:red">Error al cargar</td></tr>';
  }
}

function renderTabla(tareas) {
  const tbody = document.getElementById('filas-pedidos');
  if (!tareas.length) {
    tbody.innerHTML = '<tr><td colspan="5">Sin pedidos pendientes 🎉</td></tr>';
    return;
  }
  tbody.innerHTML = tareas.map((t,i) => `
    <tr>
      <td>${i+1}</td>
      <td><code>${t.orderId}</code></td>
      <td>${PILL[t.estado]||t.estado}</td>
      <td>${t.workerId||'—'}</td>
      <td>${SIGUIENTE[t.estado]
        ? `<button class="pp-btn pp-btn--primary"
             onclick="avanzar('${t.orderId}','${t.estado}')">
             ✅ Avanzar → ${SIGUIENTE[t.estado]}</button>`
        : '—'}</td>
    </tr>`).join('');
}

async function avanzar(orderId, estado) {
  if (!confirm(`¿Completar "${estado}" para ${orderId}?`)) return;
  const res  = await fetch(`${API_URL}/tasks/completar`, {
    method: 'POST',
    headers: {'Content-Type':'application/json'},
    body: JSON.stringify({orderId, estado})
  });
  const data = await res.json();
  data.ok ? (alert('✅ Avanzado'), cargarPedidos()) : alert(`❌ ${data.error}`);
}

cargarPedidos();
setInterval(cargarPedidos, 15000);
