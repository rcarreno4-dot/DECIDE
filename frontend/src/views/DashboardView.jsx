import React from 'react';
import { Sparkles, Trophy, History, Brain, ChevronRight, Target, Award, ArrowUpRight } from 'lucide-react';

export default function DashboardView({ usuario, onIniciarTest, onVerResultados, onVerLogros, onVerHistorial }) {
  const progresoNivel = usuario.progreso_nivel || { progreso: 0, siguiente_nivel: 'Principiante', icono_siguiente: '🌱' };

  return (
    <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-8 animate-fade-in">
      
      {/* Banner de Bienvenida con Estado de Nivel */}
      <div className="relative overflow-hidden rounded-3xl glass-panel border border-brand-500/20 p-6 sm:p-8">
        <div className="absolute top-0 right-0 -mt-10 -mr-10 w-64 h-64 bg-gradient-to-br from-brand-600/20 via-indigo-600/10 to-transparent rounded-full blur-3xl pointer-events-none" />
        
        <div className="relative z-10 grid grid-cols-1 lg:grid-cols-12 gap-6 items-center">
          <div className="lg:col-span-7 space-y-3">
            <div className="inline-flex items-center space-x-2 px-3 py-1 rounded-full bg-brand-500/15 border border-brand-500/30 text-brand-300 text-xs font-semibold">
              <span>{usuario.info_nivel?.icono || '🌱'} Nivel Actual: {usuario.info_nivel?.nombre || 'Novato'}</span>
            </div>
            
            <h1 className="text-3xl sm:text-4xl font-black text-white tracking-tight">
              ¡Hola, {usuario.nombre}! 👋
            </h1>
            <p className="text-sm text-slate-300 max-w-xl">
              Bienvenido a tu panel de competencias emocionales. Completa evaluaciones para medir tu progreso, ganar puntos y desbloquear logros en tu camino a <strong>Maestro</strong>.
            </p>

            {/* Barra de progreso de nivel */}
            <div className="pt-2 max-w-md">
              <div className="flex justify-between text-xs font-medium mb-1.5">
                <span className="text-slate-400">Progreso hacia <strong>{progresoNivel.icono_siguiente} {progresoNivel.siguiente_nivel}</strong></span>
                <span className="text-brand-400 font-bold">{progresoNivel.progreso}%</span>
              </div>
              <div className="w-full h-3 rounded-full bg-slate-800 overflow-hidden p-0.5 border border-slate-700">
                <div 
                  className="h-full rounded-full bg-gradient-to-r from-brand-500 via-indigo-500 to-cyan-400 transition-all duration-700 ease-out shadow-sm shadow-brand-500/50"
                  style={{ width: `${progresoNivel.progreso}%` }}
                />
              </div>
            </div>
          </div>

          <div className="lg:col-span-5 flex flex-col sm:flex-row lg:flex-col gap-3 justify-center">
            <button
              onClick={onIniciarTest}
              className="py-4 px-6 rounded-2xl bg-gradient-to-r from-brand-600 via-indigo-600 to-cyan-500 hover:from-brand-500 hover:to-cyan-400 text-white font-extrabold text-base shadow-xl shadow-brand-500/25 flex items-center justify-center space-x-3 transition-all hover:scale-[1.02] active:scale-[0.98]"
            >
              <Sparkles className="w-5 h-5 text-amber-300" />
              <span>Iniciar Nueva Evaluación</span>
              <ChevronRight className="w-5 h-5" />
            </button>

            <div className="grid grid-cols-2 gap-2">
              <div className="p-3 rounded-xl bg-slate-900/60 border border-slate-800 text-center">
                <div className="text-xs text-slate-400 font-medium">Puntos Acumulados</div>
                <div className="text-xl font-black text-amber-400 mt-0.5">🎯 {usuario.puntos}</div>
              </div>
              <div className="p-3 rounded-xl bg-slate-900/60 border border-slate-800 text-center">
                <div className="text-xs text-slate-400 font-medium">Nivel de Rango</div>
                <div className="text-xl font-black text-cyan-300 mt-0.5">{usuario.info_nivel?.icono || '🌱'} #{usuario.nivel}</div>
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Tarjetas de Accesos Rápidos */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-5">
        
        {/* Card 1: Evaluación */}
        <div 
          onClick={onIniciarTest}
          className="glass-card p-6 rounded-3xl cursor-pointer group flex flex-col justify-between border border-slate-800 hover:border-brand-500/40 relative overflow-hidden"
        >
          <div className="space-y-3">
            <div className="w-12 h-12 rounded-2xl bg-brand-500/10 border border-brand-500/30 flex items-center justify-center text-brand-400 group-hover:scale-110 transition-transform">
              <Brain className="w-6 h-6" />
            </div>
            <h3 className="text-lg font-bold text-white group-hover:text-brand-300 transition-colors">
              Test Situacional
            </h3>
            <p className="text-xs text-slate-400 leading-relaxed">
              Enfréntate a 16 escenarios cotidianos y laborales para evaluar tus 9 competencias socioemocionales.
            </p>
          </div>
          <div className="flex items-center text-xs font-semibold text-brand-400 mt-4 group-hover:translate-x-1 transition-transform">
            <span>Comenzar evaluación</span>
            <ArrowUpRight className="w-4 h-4 ml-1" />
          </div>
        </div>

        {/* Card 2: Logros y Medallas */}
        <div 
          onClick={onVerLogros}
          className="glass-card p-6 rounded-3xl cursor-pointer group flex flex-col justify-between border border-slate-800 hover:border-amber-500/40 relative overflow-hidden"
        >
          <div className="space-y-3">
            <div className="w-12 h-12 rounded-2xl bg-amber-500/10 border border-amber-500/30 flex items-center justify-center text-amber-400 group-hover:scale-110 transition-transform">
              <Trophy className="w-6 h-6" />
            </div>
            <h3 className="text-lg font-bold text-white group-hover:text-amber-300 transition-colors">
              Logros y Recompensas
            </h3>
            <p className="text-xs text-slate-400 leading-relaxed">
              Desbloquea hasta 12 insignias especiales completando evaluaciones y alcanzando puntuaciones altas.
            </p>
          </div>
          <div className="flex items-center text-xs font-semibold text-amber-400 mt-4 group-hover:translate-x-1 transition-transform">
            <span>Ver vitrina de trofeos</span>
            <ArrowUpRight className="w-4 h-4 ml-1" />
          </div>
        </div>

        {/* Card 3: Historial */}
        <div 
          onClick={onVerHistorial}
          className="glass-card p-6 rounded-3xl cursor-pointer group flex flex-col justify-between border border-slate-800 hover:border-indigo-500/40 relative overflow-hidden"
        >
          <div className="space-y-3">
            <div className="w-12 h-12 rounded-2xl bg-indigo-500/10 border border-indigo-500/30 flex items-center justify-center text-indigo-400 group-hover:scale-110 transition-transform">
              <History className="w-6 h-6" />
            </div>
            <h3 className="text-lg font-bold text-white group-hover:text-indigo-300 transition-colors">
              Historial de Resultados
            </h3>
            <p className="text-xs text-slate-400 leading-relaxed">
              Revisa tu evolución a lo largo del tiempo y compara tus puntuaciones generales históricas.
            </p>
          </div>
          <div className="flex items-center text-xs font-semibold text-indigo-400 mt-4 group-hover:translate-x-1 transition-transform">
            <span>Consultar historial</span>
            <ArrowUpRight className="w-4 h-4 ml-1" />
          </div>
        </div>

      </div>

      {/* Competencias Evaluadas (Resumen) */}
      <div className="glass-panel p-6 rounded-3xl border border-slate-800">
        <div className="flex items-center justify-between mb-4">
          <div className="flex items-center space-x-2">
            <Target className="w-5 h-5 text-brand-400" />
            <h2 className="text-lg font-bold text-white">Las 9 Competencias Evaluadas</h2>
          </div>
          <span className="text-xs text-slate-400">Modelo DECIDE</span>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3">
          {[
            { nombre: "Autoconocimiento", icono: "🧠", desc: "Reconocer emociones propias" },
            { nombre: "Autorregulación", icono: "🧘", desc: "Manejar impulsos y emociones" },
            { nombre: "Empatía", icono: "❤️", desc: "Comprender la perspectiva ajena" },
            { nombre: "Comunicación Asertiva", icono: "🗣️", desc: "Expresarse con respeto y claridad" },
            { nombre: "Trabajo en Equipo", icono: "🤝", desc: "Colaborar hacia metas comunes" },
            { nombre: "Toma de Decisiones", icono: "⚡", desc: "Analizar pros y contras antes de actuar" },
            { nombre: "Tolerancia a Frustración", icono: "🔥", desc: "Superar obstáculos con calma" },
            { nombre: "Manejo de Conflictos", icono: "⚔️", desc: "Resolver desacuerdos de forma constructiva" },
            { nombre: "Resiliencia", icono: "💪", desc: "Afrontar adversidades y fortalecerse" },
          ].map((comp, i) => (
            <div key={i} className="p-3 rounded-2xl bg-slate-900/60 border border-slate-800/80 flex items-center space-x-3">
              <span className="text-xl flex-shrink-0">{comp.icono}</span>
              <div className="min-w-0">
                <div className="text-xs font-bold text-slate-200 truncate">{comp.nombre}</div>
                <div className="text-[11px] text-slate-400 truncate">{comp.desc}</div>
              </div>
            </div>
          ))}
        </div>
      </div>

    </div>
  );
}
