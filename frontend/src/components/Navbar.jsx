import React from 'react';
import { Brain, Trophy, History, BarChart3, LogOut, Sparkles } from 'lucide-react';

export default function Navbar({ usuario, vistaActual, setVista, onCerrarSesion }) {
  if (!usuario) return null;

  const navItems = [
    { id: 'dashboard', label: 'Inicio', icon: Brain },
    { id: 'evaluacion', label: 'Test Situacional', icon: Sparkles },
    { id: 'historial', label: 'Historial', icon: History },
    { id: 'logros', label: 'Logros', icon: Trophy },
  ];

  return (
    <header className="sticky top-0 z-40 w-full glass-panel border-b border-slate-800/80 bg-slate-950/80 backdrop-blur-xl">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
        
        {/* Brand */}
        <div 
          onClick={() => setVista('dashboard')} 
          className="flex items-center space-x-3 cursor-pointer group"
        >
          <div className="w-10 h-10 rounded-xl bg-gradient-to-tr from-brand-600 via-indigo-600 to-cyan-400 p-0.5 shadow-lg shadow-brand-500/20 group-hover:scale-105 transition-transform">
            <div className="w-full h-full bg-slate-950 rounded-[10px] flex items-center justify-center">
              <span className="text-xl">🧠</span>
            </div>
          </div>
          <div>
            <div className="flex items-center space-x-1.5">
              <span className="font-extrabold text-lg tracking-tight bg-gradient-to-r from-white via-slate-200 to-slate-400 bg-clip-text text-transparent">
                DECIDE
              </span>
              <span className="text-[10px] font-bold px-1.5 py-0.5 rounded bg-brand-500/20 text-brand-400 border border-brand-500/30">
                v2.0
              </span>
            </div>
            <p className="text-[11px] text-slate-400 hidden sm:block">Inteligencia Emocional</p>
          </div>
        </div>

        {/* Navigation Tabs */}
        <nav className="hidden md:flex items-center space-x-1 bg-slate-900/60 p-1 rounded-xl border border-slate-800">
          {navItems.map((item) => {
            const Icon = item.icon;
            const activo = vistaActual === item.id;
            return (
              <button
                key={item.id}
                onClick={() => setVista(item.id)}
                className={`flex items-center space-x-2 px-3.5 py-1.5 rounded-lg text-sm font-medium transition-all ${
                  activo
                    ? 'bg-gradient-to-r from-brand-600 to-indigo-600 text-white shadow-md shadow-brand-500/20'
                    : 'text-slate-400 hover:text-white hover:bg-slate-800/60'
                }`}
              >
                <Icon className={`w-4 h-4 ${activo ? 'text-white' : 'text-slate-400'}`} />
                <span>{item.label}</span>
              </button>
            );
          })}
        </nav>

        {/* User Stats & Logout */}
        <div className="flex items-center space-x-3">
          <div className="hidden sm:flex items-center space-x-2.5 px-3 py-1.5 rounded-xl bg-slate-900/80 border border-slate-800">
            <span className="text-base">{usuario.info_nivel?.icono || '🌱'}</span>
            <div className="text-left">
              <div className="text-xs font-semibold text-white flex items-center space-x-1">
                <span>{usuario.nombre}</span>
                <span className="text-[10px] text-brand-400 font-normal">({usuario.info_nivel?.nombre || 'Novato'})</span>
              </div>
              <div className="text-[10px] text-slate-400">
                🎯 <strong className="text-amber-400">{usuario.puntos}</strong> pts
              </div>
            </div>
          </div>

          <button
            onClick={onCerrarSesion}
            title="Cambiar Usuario"
            className="p-2 rounded-xl text-slate-400 hover:text-rose-400 hover:bg-rose-500/10 border border-slate-800 hover:border-rose-500/30 transition-all"
          >
            <LogOut className="w-4 h-4" />
          </button>
        </div>

      </div>
    </header>
  );
}
