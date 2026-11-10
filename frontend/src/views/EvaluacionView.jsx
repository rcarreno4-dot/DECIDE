import React, { useState, useEffect } from 'react';
import { ArrowLeft, ArrowRight, Check, Sparkles, AlertCircle, HelpCircle } from 'lucide-react';

export default function EvaluacionView({ situaciones, onFinalizar, onCancelar }) {
  const [indiceActual, setIndiceActual] = useState(0);
  const [respuestas, setRespuestas] = useState([]); // array de { situacion_id, opcion_indice }
  const [opcionSeleccionada, setOpcionSeleccionada] = useState(null);
  const [animando, setAnimando] = useState(false);
  const [enviando, setEnviando] = useState(false);
  const [alerta, setAlerta] = useState('');

  const situacion = situaciones[indiceActual];
  const progresoPorcentaje = Math.round(((indiceActual) / situaciones.length) * 100);

  // Si ya respondió antes a esta situación (por ir atrás), preseleccionar
  useEffect(() => {
    const previa = respuestas.find(r => r.situacion_id === situacion?.id);
    if (previa !== undefined) {
      setOpcionSeleccionada(previa.opcion_indice);
    } else {
      setOpcionSeleccionada(null);
    }
  }, [indiceActual, situacion]);

  if (!situaciones || situaciones.length === 0) {
    return (
      <div className="min-h-[50vh] flex items-center justify-center">
        <div className="w-8 h-8 border-4 border-brand-500 border-t-transparent rounded-full animate-spin" />
      </div>
    );
  }

  const handleSeleccionarOpcion = (idx) => {
    setOpcionSeleccionada(idx);
    setAlerta('');
  };

  const handleSiguiente = async () => {
    if (opcionSeleccionada === null) {
      setAlerta('Por favor selecciona una de las opciones para continuar.');
      return;
    }

    // Guardar o actualizar la respuesta
    const nuevasRespuestas = [...respuestas];
    const indexExistente = nuevasRespuestas.findIndex(r => r.situacion_id === situacion.id);
    if (indexExistente >= 0) {
      nuevasRespuestas[indexExistente] = { situacion_id: situacion.id, opcion_indice: opcionSeleccionada };
    } else {
      nuevasRespuestas.push({ situacion_id: situacion.id, opcion_indice: opcionSeleccionada });
    }
    setRespuestas(nuevasRespuestas);

    // ¿Es la última situación?
    if (indiceActual === situaciones.length - 1) {
      setEnviando(true);
      try {
        await onFinalizar(nuevasRespuestas);
      } catch (err) {
        setAlerta('Error enviando la evaluación. Intenta de nuevo.');
        setEnviando(false);
      }
    } else {
      // Siguiente pregunta con animación
      setAnimando(true);
      setTimeout(() => {
        setIndiceActual(prev => prev + 1);
        setAnimando(false);
      }, 150);
    }
  };

  const handleAtras = () => {
    if (indiceActual > 0) {
      setAnimando(true);
      setTimeout(() => {
        setIndiceActual(prev => prev - 1);
        setAnimando(false);
      }, 150);
    }
  };

  // Color de badge de categoría
  const categoriaLabels = {
    laboral: { text: 'Laboral', color: 'bg-blue-500/10 text-blue-400 border-blue-500/30' },
    academico: { text: 'Académico', color: 'bg-purple-500/10 text-purple-400 border-purple-500/30' },
    relaciones: { text: 'Relaciones', color: 'bg-pink-500/10 text-pink-400 border-pink-500/30' },
    presion: { text: 'Bajo Presión', color: 'bg-amber-500/10 text-amber-400 border-amber-500/30' },
  };
  const catInfo = categoriaLabels[situacion?.categoria] || { text: situacion?.categoria || 'General', color: 'bg-brand-500/10 text-brand-400 border-brand-500/30' };

  return (
    <div className="max-w-3xl mx-auto px-4 sm:px-6 py-8 animate-fade-in">
      
      {/* Barra de Progreso y Header */}
      <div className="space-y-3 mb-6">
        <div className="flex items-center justify-between text-xs font-semibold">
          <div className="flex items-center space-x-2">
            <span className={`px-2.5 py-1 rounded-full border text-[11px] font-bold ${catInfo.color}`}>
              {catInfo.text}
            </span>
            <span className="text-slate-400">
              Situación {indiceActual + 1} de {situaciones.length}
            </span>
          </div>
          <span className="text-brand-400 font-bold">
            {progresoPorcentaje}% completado
          </span>
        </div>

        <div className="w-full h-2.5 rounded-full bg-slate-900 border border-slate-800 overflow-hidden">
          <div 
            className="h-full bg-gradient-to-r from-brand-600 via-indigo-600 to-cyan-400 rounded-full transition-all duration-300 ease-out"
            style={{ width: `${Math.max(5, ((indiceActual + 1) / situaciones.length) * 100)}%` }}
          />
        </div>
      </div>

      {/* Tarjeta de la Situación */}
      <div className={`glass-panel p-6 sm:p-8 rounded-3xl border border-slate-800 transition-all duration-200 ${animando ? 'opacity-40 scale-[0.98]' : 'opacity-100 scale-100'}`}>
        
        <h2 className="text-xl sm:text-2xl font-black text-white tracking-tight mb-4">
          {situacion.titulo}
        </h2>

        <div className="p-4 sm:p-5 rounded-2xl bg-slate-900/80 border border-slate-800/80 text-slate-200 text-sm sm:text-base leading-relaxed mb-6">
          {situacion.descripcion}
        </div>

        <div className="mb-3 flex items-center space-x-2 text-xs font-semibold text-slate-400 uppercase tracking-wider">
          <HelpCircle className="w-3.5 h-3.5 text-brand-400" />
          <span>¿Cómo actuarías en este caso?</span>
        </div>

        {/* Opciones */}
        <div className="space-y-3">
          {situacion.opciones.map((opcion, idx) => {
            const seleccionada = opcionSeleccionada === idx;
            return (
              <div
                key={idx}
                onClick={() => handleSeleccionarOpcion(idx)}
                className={`p-4 rounded-2xl border cursor-pointer transition-all duration-200 flex items-start space-x-3.5 group ${
                  seleccionada
                    ? 'bg-gradient-to-r from-brand-600/20 via-indigo-600/15 to-transparent border-brand-500 shadow-lg shadow-brand-500/10'
                    : 'bg-slate-900/50 border-slate-800 hover:border-slate-700 hover:bg-slate-900/80'
                }`}
              >
                <div className={`w-5 h-5 rounded-full border mt-0.5 flex items-center justify-center flex-shrink-0 transition-all ${
                  seleccionada
                    ? 'border-brand-400 bg-brand-500 text-white'
                    : 'border-slate-600 group-hover:border-slate-500'
                }`}>
                  {seleccionada && <Check className="w-3.5 h-3.5 stroke-[3]" />}
                </div>

                <div className={`text-sm leading-relaxed transition-colors ${
                  seleccionada ? 'text-white font-medium' : 'text-slate-300'
                }`}>
                  {opcion.texto}
                </div>
              </div>
            );
          })}
        </div>

        {/* Alerta de validación */}
        {alerta && (
          <div className="mt-4 p-3 rounded-xl bg-amber-500/10 border border-amber-500/30 text-amber-400 text-xs flex items-center space-x-2 animate-fade-in">
            <AlertCircle className="w-4 h-4 flex-shrink-0" />
            <span>{alerta}</span>
          </div>
        )}

        {/* Botones de Navegación */}
        <div className="mt-8 pt-6 border-t border-slate-800 flex items-center justify-between">
          <div>
            {indiceActual > 0 ? (
              <button
                type="button"
                onClick={handleAtras}
                className="py-2.5 px-4 rounded-xl border border-slate-700 hover:border-slate-600 text-slate-300 hover:text-white text-xs font-bold flex items-center space-x-1.5 transition-all"
              >
                <ArrowLeft className="w-4 h-4" />
                <span>Anterior</span>
              </button>
            ) : (
              <button
                type="button"
                onClick={onCancelar}
                className="py-2.5 px-4 rounded-xl text-slate-400 hover:text-slate-200 text-xs font-semibold transition-all"
              >
                Cancelar
              </button>
            )}
          </div>

          <button
            type="button"
            disabled={enviando}
            onClick={handleSiguiente}
            className="py-3 px-6 rounded-xl bg-gradient-to-r from-brand-600 to-indigo-600 hover:from-brand-500 hover:to-indigo-500 text-white font-bold text-sm shadow-lg shadow-brand-500/25 flex items-center space-x-2 transition-all active:scale-[0.98] disabled:opacity-50"
          >
            {enviando ? (
              <span className="inline-flex items-center space-x-2">
                <span className="w-4 h-4 border-2 border-white/30 border-t-white rounded-full animate-spin" />
                <span>Analizando Respuestas...</span>
              </span>
            ) : indiceActual === situaciones.length - 1 ? (
              <>
                <Sparkles className="w-4 h-4 text-amber-300" />
                <span>Finalizar y Evaluar</span>
              </>
            ) : (
              <>
                <span>Siguiente</span>
                <ArrowRight className="w-4 h-4" />
              </>
            )}
          </button>
        </div>

      </div>
    </div>
  );
}
