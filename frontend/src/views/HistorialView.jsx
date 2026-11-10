import React, { useState, useEffect } from 'react';
import { History, Calendar, Award, ArrowRight, Sparkles, ChevronRight } from 'lucide-react';
import { obtenerHistorial } from '../api';

export default function HistorialView({ usuario, onNuevaEvaluacion }) {
  const [historial, setHistorial] = useState([]);
  const [cargando, setCargando] = useState(true);

  useEffect(() => {
    async function cargar() {
      if (!usuario?.id) return;
      try {
        const res = await obtenerHistorial(usuario.id);
        setHistorial(res);
      } catch (err) {
        console.error('Error cargando historial:', err);
      } finally {
        setCargando(false);
      }
    }
    cargar();
  }, [usuario]);

  if (cargando) {
    return (
      <div className="min-h-[50vh] flex items-center justify-center">
        <div className="w-8 h-8 border-4 border-indigo-500 border-t-transparent rounded-full animate-spin" />
      </div>
    );
  }

  return (
    <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-8 animate-fade-in">
      
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <div className="inline-flex items-center space-x-1.5 px-3 py-1 rounded-full bg-indigo-500/10 border border-indigo-500/30 text-indigo-400 text-xs font-semibold mb-2">
            <History className="w-3.5 h-3.5" />
            <span>Progreso en el Tiempo</span>
          </div>
          <h1 className="text-3xl font-black text-white tracking-tight">
            Historial de Evaluaciones
          </h1>
          <p className="text-sm text-slate-400">
            Revisa tus puntuaciones registradas en la base de datos
          </p>
        </div>

        <button
          onClick={onNuevaEvaluacion}
          className="py-2.5 px-4 rounded-xl bg-gradient-to-r from-brand-600 to-indigo-600 hover:from-brand-500 hover:to-indigo-500 text-white font-bold text-xs shadow-lg shadow-brand-500/20 flex items-center space-x-2 transition-all self-start sm:self-auto"
        >
          <Sparkles className="w-4 h-4 text-amber-300" />
          <span>Nueva Evaluación</span>
        </button>
      </div>

      {historial.length === 0 ? (
        <div className="glass-panel p-12 rounded-3xl border border-slate-800 text-center space-y-4">
          <div className="w-16 h-16 rounded-2xl bg-slate-900 border border-slate-800 flex items-center justify-center mx-auto text-2xl">
            📝
          </div>
          <h3 className="text-lg font-bold text-white">
            Aún no tienes evaluaciones registradas
          </h3>
          <p className="text-xs text-slate-400 max-w-sm mx-auto">
            Completa tu primera evaluación para desbloquear insignias y comenzar a registrar tu historial.
          </p>
          <button
            onClick={onNuevaEvaluacion}
            className="py-2.5 px-5 rounded-xl bg-brand-600 hover:bg-brand-500 text-white font-bold text-xs shadow-lg shadow-brand-500/20 transition-all"
          >
            Iniciar Primera Evaluación
          </button>
        </div>
      ) : (
        <div className="space-y-4">
          {historial.map((item, idx) => {
            const fecha = new Date(item.fecha).toLocaleString('es-ES', {
              day: '2-digit',
              month: 'long',
              year: 'numeric',
              hour: '2-digit',
              minute: '2-digit'
            });

            const score = item.puntuacion_general;

            return (
              <div 
                key={item.id || idx}
                className="glass-card p-5 sm:p-6 rounded-2xl border border-slate-800 flex flex-col sm:flex-row sm:items-center justify-between gap-4"
              >
                <div className="flex items-center space-x-4">
                  <div className="w-14 h-14 rounded-2xl bg-gradient-to-tr from-brand-600 to-indigo-600 flex flex-col items-center justify-center text-white flex-shrink-0 shadow-md shadow-brand-500/20">
                    <span className="text-base font-black">{score}%</span>
                    <span className="text-[9px] uppercase font-bold text-brand-200">Score</span>
                  </div>

                  <div>
                    <div className="flex items-center space-x-2 text-xs text-slate-400 mb-1">
                      <Calendar className="w-3.5 h-3.5" />
                      <span>{fecha}</span>
                    </div>
                    <h3 className="text-base font-bold text-white">
                      Evaluación #{historial.length - idx}
                    </h3>
                  </div>
                </div>

                <div className="flex items-center space-x-2 self-end sm:self-auto">
                  <span className="text-xs font-semibold px-2.5 py-1 rounded-full bg-slate-800 text-slate-300 border border-slate-700">
                    {score >= 80 ? '🟢 Sobresaliente' : score >= 60 ? '🟡 Adecuado' : score >= 40 ? '🟠 En Desarrollo' : '🔴 Inicial'}
                  </span>
                </div>
              </div>
            );
          })}
        </div>
      )}

    </div>
  );
}
