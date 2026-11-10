import React from 'react';

export default function ScoreGauge({ percentage = 0, size = 180, strokeWidth = 14 }) {
  const radius = (size - strokeWidth) / 2;
  const circumference = 2 * Math.PI * radius;
  const offset = circumference - (percentage / 100) * circumference;

  // Determinar color por puntaje
  let strokeColor = '#3188fc'; // default
  let badgeText = 'Adecuado';
  let badgeBg = 'bg-blue-500/10 text-blue-400 border-blue-500/30';

  if (percentage <= 20) {
    strokeColor = '#ef4444';
    badgeText = 'Necesita Fortalecimiento';
    badgeBg = 'bg-rose-500/10 text-rose-400 border-rose-500/30';
  } else if (percentage <= 40) {
    strokeColor = '#f97316';
    badgeText = 'En Desarrollo';
    badgeBg = 'bg-orange-500/10 text-orange-400 border-orange-500/30';
  } else if (percentage <= 60) {
    strokeColor = '#eab308';
    badgeText = 'Nivel Adecuado';
    badgeBg = 'bg-amber-500/10 text-amber-400 border-amber-500/30';
  } else if (percentage <= 80) {
    strokeColor = '#10b981';
    badgeText = 'Nivel Alto';
    badgeBg = 'bg-emerald-500/10 text-emerald-400 border-emerald-500/30';
  } else {
    strokeColor = '#6366f1';
    badgeText = 'Nivel Sobresaliente';
    badgeBg = 'bg-indigo-500/10 text-indigo-400 border-indigo-500/30';
  }

  return (
    <div className="flex flex-col items-center justify-center">
      <div className="relative" style={{ width: size, height: size }}>
        <svg className="w-full h-full transform -rotate-90" viewBox={`0 0 ${size} ${size}`}>
          {/* Track de fondo */}
          <circle
            cx={size / 2}
            cy={size / 2}
            r={radius}
            stroke="currentColor"
            strokeWidth={strokeWidth}
            className="text-slate-800"
            fill="transparent"
          />
          {/* Círculo animado de progreso */}
          <circle
            cx={size / 2}
            cy={size / 2}
            r={radius}
            stroke={strokeColor}
            strokeWidth={strokeWidth}
            strokeDasharray={circumference}
            strokeDashoffset={offset}
            strokeLinecap="round"
            fill="transparent"
            className="transition-all duration-1000 ease-out"
          />
        </svg>

        {/* Contenido central */}
        <div className="absolute inset-0 flex flex-col items-center justify-center">
          <span className="text-4xl font-extrabold text-white tracking-tight">
            {percentage}%
          </span>
          <span className="text-[11px] font-medium text-slate-400 uppercase tracking-wider mt-0.5">
            Puntuación
          </span>
        </div>
      </div>

      <div className={`mt-3 px-3 py-1 rounded-full text-xs font-semibold border ${badgeBg}`}>
        {badgeText}
      </div>
    </div>
  );
}
