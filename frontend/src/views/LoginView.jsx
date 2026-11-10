import React, { useState } from 'react';
import { Brain, ArrowRight, Sparkles, Shield, Trophy, Activity } from 'lucide-react';

export default function LoginView({ onLogin }) {
  const [nombre, setNombre] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!nombre.trim()) {
      setError('Por favor ingresa tu nombre');
      return;
    }
    setError('');
    setLoading(true);
    try {
      await onLogin(nombre.trim());
    } catch (err) {
      setError('No se pudo iniciar sesión. Asegúrate de que el backend esté activo.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-[calc(100vh-4rem)] flex items-center justify-center p-4 sm:p-6 lg:p-8">
      <div className="max-w-4xl w-full grid grid-cols-1 lg:grid-cols-12 gap-8 items-center">
        
        {/* Columna Izquierda: Información de DECIDE */}
        <div className="lg:col-span-7 space-y-6 text-center lg:text-left">
          <div className="inline-flex items-center space-x-2 px-3 py-1.5 rounded-full bg-brand-500/10 border border-brand-500/30 text-brand-400 text-xs font-semibold">
            <Sparkles className="w-3.5 h-3.5" />
            <span>DECIDE 2.0 Web Edition</span>
          </div>

          <h1 className="text-4xl sm:text-5xl lg:text-6xl font-black tracking-tight leading-tight">
            Descubre y potencia tu{' '}
            <span className="bg-gradient-to-r from-brand-400 via-indigo-400 to-cyan-300 bg-clip-text text-transparent">
              Inteligencia Emocional
            </span>
          </h1>

          <p className="text-slate-400 text-base sm:text-lg max-w-xl">
            Evalúa tus competencias socioemocionales ante situaciones reales de la vida cotidiana y laboral con algoritmos de diagnóstico y gamificación.
          </p>

          <div className="grid grid-cols-2 sm:grid-cols-3 gap-3.5 pt-2 max-w-lg mx-auto lg:mx-0">
            <div className="glass-card p-3.5 rounded-2xl text-left">
              <Activity className="w-5 h-5 text-brand-400 mb-1.5" />
              <div className="text-sm font-bold text-white">9 Competencias</div>
              <div className="text-[11px] text-slate-400">Diagnóstico integral</div>
            </div>
            <div className="glass-card p-3.5 rounded-2xl text-left">
              <Shield className="w-5 h-5 text-emerald-400 mb-1.5" />
              <div className="text-sm font-bold text-white">16 Escenarios</div>
              <div className="text-[11px] text-slate-400">Casos reales</div>
            </div>
            <div className="glass-card p-3.5 rounded-2xl text-left col-span-2 sm:col-span-1">
              <Trophy className="w-5 h-5 text-amber-400 mb-1.5" />
              <div className="text-sm font-bold text-white">Gamificación</div>
              <div className="text-[11px] text-slate-400">12 logros y niveles</div>
            </div>
          </div>
        </div>

        {/* Columna Derecha: Tarjeta de Login */}
        <div className="lg:col-span-5 w-full max-w-md mx-auto">
          <div className="glass-panel p-6 sm:p-8 rounded-3xl border border-slate-800 shadow-2xl relative overflow-hidden">
            
            <div className="w-14 h-14 rounded-2xl bg-gradient-to-tr from-brand-600 to-indigo-600 flex items-center justify-center mx-auto mb-4 shadow-lg shadow-brand-500/25">
              <Brain className="w-7 h-7 text-white" />
            </div>

            <h2 className="text-2xl font-bold text-white text-center mb-1">
              Bienvenido a DECIDE
            </h2>
            <p className="text-xs text-slate-400 text-center mb-6">
              Ingresa tu nombre para acceder a tu perfil
            </p>

            {error && (
              <div className="mb-4 p-3 rounded-xl bg-rose-500/10 border border-rose-500/30 text-rose-400 text-xs">
                {error}
              </div>
            )}

            <form onSubmit={handleSubmit} className="space-y-4">
              <div>
                <label className="block text-xs font-semibold text-slate-300 uppercase tracking-wider mb-2">
                  Tu Nombre o Alias
                </label>
                <input
                  type="text"
                  value={nombre}
                  onChange={(e) => setNombre(e.target.value)}
                  placeholder="Ej. Fabian, Carlos, María..."
                  className="w-full px-4 py-3 rounded-xl bg-slate-900 border border-slate-700/80 focus:border-brand-500 focus:ring-2 focus:ring-brand-500/20 text-white placeholder-slate-500 text-sm outline-none transition-all"
                  autoFocus
                />
              </div>

              <button
                type="submit"
                disabled={loading}
                className="w-full py-3.5 px-4 rounded-xl bg-gradient-to-r from-brand-600 via-indigo-600 to-cyan-500 hover:from-brand-500 hover:to-cyan-400 text-white font-bold text-sm shadow-xl shadow-brand-500/20 flex items-center justify-center space-x-2 transition-all active:scale-[0.98] disabled:opacity-50"
              >
                {loading ? (
                  <span className="inline-flex items-center space-x-2">
                    <span className="w-4 h-4 border-2 border-white/30 border-t-white rounded-full animate-spin" />
                    <span>Conectando...</span>
                  </span>
                ) : (
                  <>
                    <span>Comenzar Experiencia</span>
                    <ArrowRight className="w-4 h-4" />
                  </>
                )}
              </button>
            </form>

            <p className="text-[11px] text-slate-500 text-center mt-6">
              Tus respuestas y evaluaciones quedan guardadas de manera segura en tu perfil.
            </p>
          </div>
        </div>

      </div>
    </div>
  );
}
