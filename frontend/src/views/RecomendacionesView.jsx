import React from 'react';
import { ArrowLeft, Target, CheckCircle2, TrendingUp, AlertTriangle, ShieldCheck, Sparkles } from 'lucide-react';

export default function RecomendacionesView({ data, onVolverResultados }) {
  if (!data) return null;

  const { recomendaciones, plan_desarrollo, proximos_pasos } = data;
  const recomendacionesArray = Object.entries(recomendaciones || {}).map(([key, value]) => ({
    key,
    ...value
  }));

  return (
    <div className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-8 animate-fade-in">
      
      {/* Botón Volver y Encabezado */}
      <div>
        <button
          onClick={onVolverResultados}
          className="mb-4 inline-flex items-center space-x-1.5 text-xs font-semibold text-slate-400 hover:text-white transition-colors"
        >
          <ArrowLeft className="w-4 h-4" />
          <span>Volver al Perfil de Resultados</span>
        </button>

        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
          <div>
            <h1 className="text-3xl font-black text-white tracking-tight">
              💡 Plan de Desarrollo y Recomendaciones
            </h1>
            <p className="text-sm text-slate-400 mt-1">
              Estrategias personalizadas basadas en el análisis de tus respuestas
            </p>
          </div>
        </div>
      </div>

      {/* Plan de Desarrollo (Enfoque, Secundarios y Fortalezas) */}
      {plan_desarrollo && (
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          
          {/* Enfoque Principal */}
          {plan_desarrollo.enfoque_principal && (
            <div className="glass-card p-5 rounded-2xl border border-rose-500/30 bg-rose-500/5">
              <div className="flex items-center space-x-2 text-rose-400 mb-2">
                <AlertTriangle className="w-4 h-4" />
                <span className="text-xs font-bold uppercase tracking-wider">Área Prioritaria</span>
              </div>
              <h3 className="text-base font-extrabold text-white">
                {plan_desarrollo.enfoque_principal[1]?.nombre}
              </h3>
              <div className="text-2xl font-black text-rose-400 my-1">
                {plan_desarrollo.enfoque_principal[1]?.puntuacion_normalizada}%
              </div>
              <p className="text-xs text-slate-400">
                Esta competencia representa tu mayor oportunidad de crecimiento inmediato.
              </p>
            </div>
          )}

          {/* Secundarios */}
          <div className="glass-card p-5 rounded-2xl border border-amber-500/30 bg-amber-500/5">
            <div className="flex items-center space-x-2 text-amber-400 mb-2">
              <TrendingUp className="w-4 h-4" />
              <span className="text-xs font-bold uppercase tracking-wider">En Desarrollo</span>
            </div>
            <div className="space-y-2">
              {plan_desarrollo.secundarios?.map(([key, val], idx) => (
                <div key={idx} className="flex justify-between items-center text-xs">
                  <span className="text-white font-medium truncate">{val.nombre}</span>
                  <span className="font-bold text-amber-400">{val.puntuacion_normalizada}%</span>
                </div>
              ))}
            </div>
            <p className="text-xs text-slate-400 mt-3">
              Competencias con buen margen de optimización en el corto plazo.
            </p>
          </div>

          {/* Fortalezas Clave */}
          <div className="glass-card p-5 rounded-2xl border border-emerald-500/30 bg-emerald-500/5">
            <div className="flex items-center space-x-2 text-emerald-400 mb-2">
              <ShieldCheck className="w-4 h-4" />
              <span className="text-xs font-bold uppercase tracking-wider">Tus Mayores Fortalezas</span>
            </div>
            <div className="space-y-2">
              {plan_desarrollo.fortalezas?.map(([key, val], idx) => (
                <div key={idx} className="flex justify-between items-center text-xs">
                  <span className="text-white font-medium truncate">{val.nombre}</span>
                  <span className="font-bold text-emerald-400">{val.puntuacion_normalizada}%</span>
                </div>
              ))}
            </div>
            <p className="text-xs text-slate-400 mt-3">
              Puntos fuertes que puedes apalancar para liderar y mediar con éxito.
            </p>
          </div>

        </div>
      )}

      {/* Próximos Pasos de Acción */}
      {proximos_pasos && proximos_pasos.length > 0 && (
        <div className="glass-panel p-6 rounded-3xl border border-slate-800">
          <div className="flex items-center space-x-2 mb-4">
            <Target className="w-5 h-5 text-brand-400" />
            <h2 className="text-lg font-bold text-white">
              Próximos Pasos Sugeridos
            </h2>
          </div>

          <div className="space-y-3">
            {proximos_pasos.map((paso, idx) => {
              const esAlta = paso.prioridad === 'ALTA';
              return (
                <div 
                  key={idx}
                  className="p-4 rounded-2xl bg-slate-900/60 border border-slate-800/80 flex flex-col sm:flex-row sm:items-center justify-between gap-3"
                >
                  <div className="space-y-1">
                    <div className="flex items-center space-x-2">
                      <span className={`text-[10px] font-bold px-2 py-0.5 rounded-full border ${
                        esAlta 
                          ? 'bg-rose-500/10 text-rose-400 border-rose-500/30' 
                          : 'bg-amber-500/10 text-amber-400 border-amber-500/30'
                      }`}>
                        Prioridad {paso.prioridad}
                      </span>
                      <span className="text-sm font-bold text-white">{paso.competencia}</span>
                    </div>
                    <p className="text-xs text-slate-300">
                      {paso.accion}
                    </p>
                  </div>

                  <div className="px-3 py-1.5 rounded-xl bg-slate-800/60 text-right sm:text-center flex-shrink-0">
                    <div className="text-[10px] text-slate-400">Meta Sugerida</div>
                    <div className="text-xs font-bold text-cyan-300">{paso.meta}</div>
                  </div>
                </div>
              );
            })}
          </div>
        </div>
      )}

      {/* Consejos por Competencia */}
      <div>
        <h2 className="text-lg font-bold text-white mb-4">
          Guía de Práctica por Competencia
        </h2>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          {recomendacionesArray.map((rec) => (
            <div 
              key={rec.key}
              className="glass-card p-5 rounded-2xl border border-slate-800 space-y-2.5"
            >
              <div className="flex items-center justify-between">
                <h3 className="text-sm font-bold text-white">
                  {rec.nombre}
                </h3>
                <span className="text-xs font-semibold text-brand-400">
                  {rec.puntuacion}%
                </span>
              </div>

              <p className="text-xs text-slate-300 leading-relaxed">
                {rec.recomendacion}
              </p>
            </div>
          ))}
        </div>
      </div>

    </div>
  );
}
