import React, { useState, useEffect } from 'react';
import { Trophy, Lock, CheckCircle, Award, Sparkles } from 'lucide-react';
import { obtenerLogros } from '../api';

export default function LogrosView({ usuario }) {
  const [datosLogros, setDatosLogros] = useState(null);
  const [cargando, setCargando] = useState(true);

  useEffect(() => {
    async function cargar() {
      if (!usuario?.id) return;
      try {
        const res = await obtenerLogros(usuario.id);
        setDatosLogros(res);
      } catch (err) {
        console.error('Error cargando logros:', err);
      } finally {
        setCargando(false);
      }
    }
    cargar();
  }, [usuario]);

  if (cargando) {
    return (
      <div className="min-h-[50vh] flex items-center justify-center">
        <div className="w-8 h-8 border-4 border-amber-500 border-t-transparent rounded-full animate-spin" />
      </div>
    );
  }

  const logros = datosLogros?.logros || [];
  const totalDesbloqueados = datosLogros?.total_desbloqueados || 0;
  const progresoNivel = datosLogros?.progreso_nivel || usuario.progreso_nivel || { progreso: 0, siguiente_nivel: 'Principiante', icono_siguiente: '🌱' };

  return (
    <div className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-8 animate-fade-in">
      
      {/* Banner de Rango y Puntos */}
      <div className="glass-panel p-6 sm:p-8 rounded-3xl border border-amber-500/20 relative overflow-hidden">
        <div className="absolute top-0 right-0 -mr-16 -mt-16 w-64 h-64 bg-amber-500/10 rounded-full blur-3xl pointer-events-none" />

        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-6">
          <div className="space-y-2">
            <div className="inline-flex items-center space-x-1.5 px-3 py-1 rounded-full bg-amber-500/10 border border-amber-500/30 text-amber-400 text-xs font-semibold">
              <Trophy className="w-3.5 h-3.5" />
              <span>Vitrina de Logros DECIDE</span>
            </div>

            <h1 className="text-3xl font-black text-white tracking-tight">
              Tus Insignias y Rango
            </h1>

            <p className="text-sm text-slate-300 max-w-xl">
              Has desbloqueado <strong>{totalDesbloqueados} de {logros.length}</strong> insignias emocionales.
            </p>
          </div>

          <div className="flex items-center space-x-4 p-4 rounded-2xl bg-slate-900/80 border border-slate-800 flex-shrink-0">
            <div className="text-4xl">{datosLogros?.info_nivel?.icono || '🌱'}</div>
            <div>
              <div className="text-xs text-slate-400 uppercase font-semibold">Rango Actual</div>
              <div className="text-lg font-black text-white">{datosLogros?.info_nivel?.nombre || 'Novato'}</div>
              <div className="text-xs text-amber-400 font-bold">🎯 {datosLogros?.puntos || 0} pts acumulados</div>
            </div>
          </div>
        </div>

        {/* Barra de progreso hacia el siguiente nivel */}
        <div className="mt-6 pt-6 border-t border-slate-800/80">
          <div className="flex justify-between text-xs font-medium mb-1.5">
            <span className="text-slate-400">Progreso a <strong>{progresoNivel.icono_siguiente} {progresoNivel.siguiente_nivel}</strong></span>
            <span className="text-amber-400 font-bold">{progresoNivel.progreso}%</span>
          </div>
          <div className="w-full h-2.5 rounded-full bg-slate-900 overflow-hidden border border-slate-800">
            <div 
              className="h-full rounded-full bg-gradient-to-r from-amber-500 via-yellow-400 to-emerald-400 transition-all duration-700 ease-out"
              style={{ width: `${progresoNivel.progreso}%` }}
            />
          </div>
        </div>
      </div>

      {/* Grid de los 12 Logros */}
      <div>
        <div className="flex items-center justify-between mb-4">
          <h2 className="text-xl font-bold text-white tracking-tight">
            Colección de Insignias (12)
          </h2>
          <span className="text-xs text-slate-400">Gana 100 pts por evaluación</span>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
          {logros.map((item) => {
            const desbloqueado = item.desbloqueado;
            return (
              <div
                key={item.tipo}
                className={`p-5 rounded-2xl border transition-all duration-300 flex flex-col justify-between ${
                  desbloqueado
                    ? 'glass-card border-amber-500/40 bg-gradient-to-b from-amber-500/10 via-slate-900/60 to-slate-900/80 shadow-lg shadow-amber-500/5'
                    : 'bg-slate-900/30 border-slate-800/60 opacity-60'
                }`}
              >
                <div>
                  <div className="flex items-start justify-between mb-3">
                    <div className={`w-12 h-12 rounded-xl flex items-center justify-center text-2xl ${
                      desbloqueado ? 'bg-amber-500/20 border border-amber-500/40' : 'bg-slate-800 border border-slate-700'
                    }`}>
                      {desbloqueado ? item.icono : <Lock className="w-5 h-5 text-slate-500" />}
                    </div>

                    {desbloqueado ? (
                      <span className="inline-flex items-center space-x-1 px-2 py-0.5 rounded-full bg-emerald-500/15 border border-emerald-500/30 text-emerald-400 text-[10px] font-bold">
                        <CheckCircle className="w-3 h-3" />
                        <span>Desbloqueado</span>
                      </span>
                    ) : (
                      <span className="px-2 py-0.5 rounded-full bg-slate-800 text-slate-400 text-[10px] font-medium border border-slate-700">
                        Bloqueado
                      </span>
                    )}
                  </div>

                  <h3 className={`text-sm font-bold mb-1 ${desbloqueado ? 'text-white' : 'text-slate-400'}`}>
                    {item.nombre}
                  </h3>

                  <p className="text-xs text-slate-400 leading-relaxed mb-4">
                    {item.descripcion}
                  </p>
                </div>

                {desbloqueado && item.fecha && (
                  <div className="pt-2 border-t border-slate-800/60 text-[10px] text-slate-500">
                    Obtenido el {new Date(item.fecha).toLocaleDateString('es-ES', { day: '2-digit', month: 'short', year: 'numeric' })}
                  </div>
                )}
              </div>
            );
          })}
        </div>
      </div>

    </div>
  );
}
