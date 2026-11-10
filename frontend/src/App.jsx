import React, { useState, useEffect } from 'react';
import Navbar from './components/Navbar';
import AchievementModal from './components/AchievementModal';
import LoginView from './views/LoginView';
import DashboardView from './views/DashboardView';
import EvaluacionView from './views/EvaluacionView';
import ResultadosView from './views/ResultadosView';
import RecomendacionesView from './views/RecomendacionesView';
import LogrosView from './views/LogrosView';
import HistorialView from './views/HistorialView';

import { loginUsuario, obtenerSituaciones, enviarEvaluacion } from './api';

export default function App() {
  const [usuario, setUsuario] = useState(() => {
    const guardado = localStorage.getItem('decide_usuario');
    return guardado ? JSON.parse(guardado) : null;
  });

  const [vista, setVista] = useState(() => (usuario ? 'dashboard' : 'login'));
  const [situaciones, setSituaciones] = useState([]);
  const [resultadoData, setResultadoData] = useState(null);
  const [nuevosLogros, setNuevosLogros] = useState([]);
  const [cargandoGlobal, setCargandoGlobal] = useState(false);

  // Cargar situaciones al iniciar
  useEffect(() => {
    async function cargar() {
      try {
        const datos = await obtenerSituaciones();
        setSituaciones(datos);
      } catch (e) {
        console.error('Error cargando situaciones:', e);
      }
    }
    cargar();
  }, []);

  // Guardar usuario en localStorage
  useEffect(() => {
    if (usuario) {
      localStorage.setItem('decide_usuario', JSON.stringify(usuario));
    } else {
      localStorage.removeItem('decide_usuario');
    }
  }, [usuario]);

  const handleLogin = async (nombre) => {
    const usuarioRes = await loginUsuario(nombre);
    setUsuario(usuarioRes);
    setVista('dashboard');
  };

  const handleCerrarSesion = () => {
    setUsuario(null);
    setVista('login');
    setResultadoData(null);
  };

  const handleFinalizarEvaluacion = async (respuestas) => {
    if (!usuario?.id) return;
    setCargandoGlobal(true);
    try {
      const data = await enviarEvaluacion(usuario.id, respuestas);
      setResultadoData(data);
      
      // Actualizar puntos y nivel del usuario en tiempo real
      if (data.gamificacion) {
        setUsuario(prev => ({
          ...prev,
          puntos: data.gamificacion.puntos,
          nivel: data.gamificacion.nivel,
          info_nivel: data.gamificacion.info_nivel,
          progreso_nivel: {
            progreso: data.gamificacion.progreso,
            siguiente_nivel: data.gamificacion.siguiente_nivel,
            icono_siguiente: data.gamificacion.icono_siguiente,
          }
        }));
      }

      // Si hay nuevos logros, disparar modal de celebración
      if (data.nuevos_logros && data.nuevos_logros.length > 0) {
        setNuevosLogros(data.nuevos_logros);
      }

      setVista('resultados');
    } finally {
      setCargandoGlobal(false);
    }
  };

  return (
    <div className="min-h-screen flex flex-col bg-slate-950 text-slate-100 selection:bg-brand-500 selection:text-white">
      {/* Barra de Navegación superior */}
      <Navbar
        usuario={usuario}
        vistaActual={vista}
        setVista={setVista}
        onCerrarSesion={handleCerrarSesion}
      />

      {/* Contenido Dinámico de la Vista */}
      <main className="flex-1 pb-16">
        {!usuario || vista === 'login' ? (
          <LoginView onLogin={handleLogin} />
        ) : vista === 'dashboard' ? (
          <DashboardView
            usuario={usuario}
            onIniciarTest={() => setVista('evaluacion')}
            onVerResultados={() => resultadoData ? setVista('resultados') : setVista('evaluacion')}
            onVerLogros={() => setVista('logros')}
            onVerHistorial={() => setVista('historial')}
          />
        ) : vista === 'evaluacion' ? (
          <EvaluacionView
            situaciones={situaciones}
            onFinalizar={handleFinalizarEvaluacion}
            onCancelar={() => setVista('dashboard')}
          />
        ) : vista === 'resultados' ? (
          <ResultadosView
            data={resultadoData}
            onVerRecomendaciones={() => setVista('recomendaciones')}
            onReiniciarTest={() => setVista('evaluacion')}
            onIrDashboard={() => setVista('dashboard')}
          />
        ) : vista === 'recomendaciones' ? (
          <RecomendacionesView
            data={resultadoData}
            onVolverResultados={() => setVista('resultados')}
          />
        ) : vista === 'logros' ? (
          <LogrosView usuario={usuario} />
        ) : vista === 'historial' ? (
          <HistorialView
            usuario={usuario}
            onNuevaEvaluacion={() => setVista('evaluacion')}
          />
        ) : null}
      </main>

      {/* Modal de Nuevos Logros Desbloqueados con Confetti */}
      {nuevosLogros.length > 0 && (
        <AchievementModal
          logros={nuevosLogros}
          onClose={() => setNuevosLogros([])}
        />
      )}

      {/* Footer minimalista */}
      <footer className="py-6 border-t border-slate-900 text-center text-xs text-slate-500">
        <p>DECIDE v2.0 Web Edition • Evaluador de Competencias Emocionales con React & Tailwind</p>
      </footer>
    </div>
  );
}
