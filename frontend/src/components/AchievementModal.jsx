import React, { useEffect } from 'react';
import confetti from 'canvas-confetti';
import { Trophy, CheckCircle, Sparkles, X } from 'lucide-react';

export default function AchievementModal({ logros, onClose }) {
  if (!logros || logros.length === 0) return null;

  useEffect(() => {
    // Disparo de confetti festivo
    try {
      confetti({
        particleCount: 100,
        spread: 70,
        origin: { y: 0.6 },
        colors: ['#3188fc', '#2ecc71', '#f59e0b', '#ec4899', '#8b5cf6']
      });
    } catch (e) {
      console.log('Confetti effect:', e);
    }
  }, [logros]);

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-950/80 backdrop-blur-md animate-fade-in">
      <div className="relative w-full max-w-md bg-gradient-to-b from-slate-900 via-slate-900 to-slate-950 border border-brand-500/30 rounded-3xl p-6 sm:p-8 shadow-2xl shadow-brand-500/10 animate-pop-in text-center">
        
        {/* Glow orb */}
        <div className="absolute -top-12 left-1/2 -translate-x-1/2 w-24 h-24 bg-brand-500/20 rounded-full blur-2xl pointer-events-none" />

        {/* Icon banner */}
        <div className="mx-auto w-16 h-16 rounded-2xl bg-gradient-to-tr from-amber-500 to-yellow-300 p-0.5 shadow-xl shadow-amber-500/30 flex items-center justify-center mb-5 animate-bounce">
          <Trophy className="w-8 h-8 text-slate-950" />
        </div>

        <div className="inline-flex items-center space-x-1.5 px-3 py-1 rounded-full bg-amber-500/10 border border-amber-500/30 text-amber-400 text-xs font-semibold mb-2">
          <Sparkles className="w-3.5 h-3.5" />
          <span>¡NUEVO LOGRO DESBLOQUEADO!</span>
        </div>

        <h3 className="text-xl sm:text-2xl font-extrabold text-white mb-2">
          {logros.length === 1 ? '¡Felicitaciones!' : `¡Desbloqueaste ${logros.length} Logros!`}
        </h3>
        
        <p className="text-sm text-slate-400 mb-6">
          Tu evolución en competencias emocionales sigue dando frutos.
        </p>

        {/* Lista de logros */}
        <div className="space-y-3 mb-6 text-left max-h-60 overflow-y-auto pr-1">
          {logros.map((logro, idx) => (
            <div 
              key={idx}
              className="flex items-center space-x-3.5 p-3.5 rounded-2xl bg-slate-800/60 border border-slate-700/80"
            >
              <div className="w-11 h-11 rounded-xl bg-slate-700/80 flex items-center justify-center text-2xl flex-shrink-0">
                {logro.icono || '🏆'}
              </div>
              <div className="flex-1 min-w-0">
                <h4 className="text-sm font-bold text-slate-100 truncate">
                  {logro.nombre}
                </h4>
                <p className="text-xs text-slate-400 line-clamp-2">
                  {logro.descripcion}
                </p>
              </div>
              <CheckCircle className="w-5 h-5 text-emerald-400 flex-shrink-0" />
            </div>
          ))}
        </div>

        <button
          onClick={onClose}
          className="w-full py-3 px-5 rounded-xl bg-gradient-to-r from-brand-600 to-indigo-600 hover:from-brand-500 hover:to-indigo-500 text-white font-bold text-sm shadow-lg shadow-brand-500/25 transition-all active:scale-[0.98]"
        >
          ¡Continuar y Explorar!
        </button>
      </div>
    </div>
  );
}
