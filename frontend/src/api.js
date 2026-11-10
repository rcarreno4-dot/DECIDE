// api.js - Cliente API para comunicarse con app_web.py

const API_BASE = '/api';

export async function loginUsuario(nombre) {
  const res = await fetch(`${API_BASE}/usuario/login`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ nombre })
  });
  if (!res.ok) throw new Error('Error al iniciar sesión');
  return res.json();
}

export async function obtenerSituaciones() {
  const res = await fetch(`${API_BASE}/situaciones`);
  if (!res.ok) throw new Error('Error al obtener situaciones');
  return res.json();
}

export async function obtenerCompetencias() {
  const res = await fetch(`${API_BASE}/competencias`);
  if (!res.ok) throw new Error('Error al obtener competencias');
  return res.json();
}

export async function enviarEvaluacion(usuario_id, respuestas) {
  const res = await fetch(`${API_BASE}/evaluacion/enviar`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ usuario_id, respuestas })
  });
  if (!res.ok) throw new Error('Error al procesar la evaluación');
  return res.json();
}

export async function obtenerHistorial(usuario_id) {
  const res = await fetch(`${API_BASE}/usuario/${usuario_id}/historial`);
  if (!res.ok) throw new Error('Error al obtener historial');
  return res.json();
}

export async function obtenerLogros(usuario_id) {
  const res = await fetch(`${API_BASE}/usuario/${usuario_id}/logros`);
  if (!res.ok) throw new Error('Error al obtener logros');
  return res.json();
}
