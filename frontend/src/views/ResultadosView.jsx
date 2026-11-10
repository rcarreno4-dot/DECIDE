import React from 'react';
import ScoreGauge from '../components/ScoreGauge';
import { ArrowRight, Lightbulb, RotateCcw, Home, Sparkles, Award } from 'lucide-react';

export default function ResultadosView({ data, onVerRecomendaciones, onReiniciarTest, onIrDashboard }) {
  if (!data) return null;

  const { resultados, puntuacion_general, gamificacion } = data;

  const competenciasArray = Object.entries(resultados || {}).map(([key, value]) => ({
    key,
    ...value
  }));

  return (
    <div className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-8 animate-fade-in">
      
      {/* Encabezado Principal con Medidor */}
      <div className="glass-panel p-6 sm:p-8 rounded-3xl border border-brand-500/20 relative overflow-hidden">
        <div className="absolute top-0 right-0 -mr-16 -mt-16 w-64 h-64 bg-brand-500/10 rounded-full blur-3xl pointer-events-none" />

        <div className="grid grid-cols-1 md:grid-cols-12 gap-6 items-center">
          
          <div className="md:col-span-5 flex flex-col items-center justify-center p-4">
            <ScoreGauge percentage={puntuacion_general || 0} size={190} strokeWidth={15} />
          </div>

          <div className="md:col-span-7 space-y-4 text-center md:text-left">
            <div className="inline-flex items-center space-x-1.5 px-3 py-1 rounded-full bg-emerald-500/10 border border-emerald-500/30 text-emerald-400 text-xs font-semibold">
              <Sparkles className="w-3.5 h-3.5" />
              <span>¡Evaluación Completada con Éxito!</span>
            </div>

            <h1 className="text-3xl sm:text-4xl font-black text-white tracking-tight">
              Tu Perfil DECIDE de Inteligencia Emocional
            </h1>

            <p className="text-sm text-slate-300">
              Has completado el diagnóstico situacional. Tus respuestas han sido analizadas bajo el modelo DECIDE normalizado a escala de 0 a 100%.
            </p>

            <div className="p-3.5 rounded-2xl bg-slate-900/80 border border-slate-800 flex items-center justify-between text-xs">
              <div className="flex items-center space-x-2">
                <span className="text-lg">🎯</span>
                <span className="text-slate-300">Has ganado <strong>+100 puntos</strong> por esta evaluación</span>
              </div>
              <span className="font-bold text-amber-400">Total: {gamificacion?.puntos || 0} pts</span>
            </div>

            <div className="pt-2 flex flex-wrap gap-3 justify-center md:justify-start">
              <button
                onClick={onVerRecomendaciones}
                className="py-3 px-5 rounded-xl bg-gradient-to-r from-brand-600 to-indigo-600 hover:from-brand-500 hover:to-indigo-500 text-white font-bold text-xs shadow-lg shadow-brand-500/25 flex items-center space-x-2 transition-all active:scale-[0.98]"
              >
                <Lightbulb className="w-4 h-4 text-yellow-300" />
                <span>Ver Recomendaciones y Plan de Acción</span>
                <ArrowRight className="w-4 h-4" />
              </button>

              <button
                onClick={onIrDashboard}
                className="py-3 px-4 rounded-xl border border-slate-700 hover:border-slate-600 text-slate-300 hover:text-white text-xs font-semibold flex items-center space-x-1.5 transition-all"
              >
                <Home className="w-4 h-4" />
                <span>Volver al Inicio</span>
              </button>
            </div>
          </div>

        </div>
      </div>

      {/* Desglose de las 9 Competencias */}
      <div>
        <div className="flex items-center justify-between mb-4">
          <h2 className="text-xl font-bold text-white tracking-tight">
            Desglose de Competencias Emocionales
          </h2>
          <span className="text-xs text-slate-400">Escala de 0 a 100%</span>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {competenciasArray.map((comp) => {
            const pct = comp.puntuacion_normalizada || 0;
            
            // Color de la barra
            let barColor = 'from-blue-500 to-cyan-400';
            let badgeBg = 'bg-blue-500/10 text-blue-400 border-blue-500/30';
            if (pct <= 20) {
              barColor = 'from-rose-500 to-red-400';
              badgeBg = 'bg-rose-500/10 text-rose-400 border-rose-500/30';
            } else if (pct <= 40) {
              barColor = 'from-orange-500 to-amber-400';
              badgeBg = 'bg-orange-500/10 text-orange-400 border-orange-500/30';
            } else if (pct <= 60) {
              barColor = 'from-amber-500 to-yellow-400';
              badgeBg = 'bg-amber-500/10 text-amber-400 border-amber-500/30';
            } else if (pct <= 80) {
              barColor = 'from-emerald-500 to-teal-400';
              badgeBg = 'bg-emerald-500/10 text-emerald-400 border-emerald-500/30';
            } else {
              barColor = 'from-indigo-500 to-purple-400';
              badgeBg = 'bg-indigo-500/10 text-indigo-400 border-indigo-500/30';
            }

            return (
              <div 
                key={comp.key} 
                className="glass-card p-5 rounded-2xl border border-slate-800 flex flex-col justify-between"
              >
                <div>
                  <div className="flex items-start justify-between gap-2 mb-2">
                    <h3 className="text-sm font-bold text-white">
                      {comp.nombre}
                    </h3>
                    <span className="text-sm font-black text-brand-400">
                      {pct}%
                    </span>
                  </div>

                  <p className="text-[11px] text-slate-400 line-clamp-2 mb-3">
                    {comp.descripcion}
                  </p>
                </div>

                <div>
                  {/* Barra de progreso */}
                  <div className="w-full h-2 rounded-full bg-slate-800 overflow-hidden mb-2.5">
                    <div 
                      className={`h-full rounded-full bg-gradient-to-r ${barColor} transition-all duration-700 ease-out`}
                      style={{ width: `${Math.max(4, pct)}%` }}
                    />
                  </div>

                  <div className="flex items-center justify-between">
                    <span className={`text-[10px] font-semibold px-2 py-0.5 rounded-full border ${badgeBg}`}>
                      {comp.nivel?.nivel || 'Adecuado'}
                    </span>
                    <span className="text-[10px] text-slate-500">
                      {comp.puntuacion_total} pts brutos
                    </span>
                  </div>
                </div>
              </div>
            );
          })}
        </div>
      </div>

    </div>
  );
}
