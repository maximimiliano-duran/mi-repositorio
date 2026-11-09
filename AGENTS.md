# Instrucciones del proyecto

## Base confirmada

- El juego se desarrollará en Unity con C#.
- El concepto combina combate de magia elemental, partidas repetibles con estructura roguelite y humor vulgar con modismos chilenos.
- El protagonista es un estudiante subestimado que descubre su potencial. El «sistema» es una mecánica y recurso narrativo ficticio; no se integrará un servicio de IA.
- La primera muestra propuesta contiene un personaje controlable, un elemento con ataque básico y habilidad, esquive, una sala, un enemigo, vida y daño, derrota, recompensa con elección y reinicio.

## Reglas de trabajo

- Trata toda decisión no confirmada como propuesta. No inventes el nombre del juego, estilo artístico, cámara, 2D o 3D, plataformas, controles, duración de partidas ni presupuesto.
- No incorpores personajes, escenarios, código ni recursos de otros proyectos del repositorio original.
- No implementes progresión permanente después de morir hasta que se acuerde qué persiste.
- Antes de construir el sistema elemental completo, presenta opciones concretas y sus consecuencias para elemento del protagonista, elementos disponibles, combinaciones, habilidades, recursos, recargas y estados.
- No compres recursos. Antes de integrar assets, verifica versión de Unity, pipeline, coherencia visual, materiales, animaciones, dependencias, esfuerzo de adaptación, precio, procedencia y licencia. Identifica los recursos provisionales.
- Realiza cambios pequeños y verificables. Distingue código escrito, compilación y comportamiento comprobado en el Editor.
- Registra aquí las decisiones confirmadas y mantén el historial en Git.

## Decisiones confirmadas para la muestra

- Nombre técnico del proyecto: `PrototipoElemental`. El nombre comercial del juego sigue pendiente.
- Presentación: juego 3D con cámara cenital y dirección artística ilustrada en 2D.
- Plataforma inicial: Windows PC. Monetización aún no definida.
- Editor: Unity 6.3 LTS, versión `6000.3.28f1`.
- Pipeline: Universal Render Pipeline, plantilla oficial `com.unity.template.urp-blank`.
- Alcance: una sala, personaje controlable, ataque y habilidad de un elemento, esquive, un enemigo, vida y daño, derrota, recompensa con elección y reinicio.

## Pendiente de decisión

- Nombre comercial, identidad artística final y recursos definitivos.
- Elemento del protagonista, elementos disponibles, combinaciones, habilidades, recursos, recargas y estados.
- Qué se conserva después de morir. No implementes progresión permanente hasta acordarlo.
- Duración de las partidas y plataforma final además de Windows PC.

## Estado técnico

- El proyecto Unity está en `PrototipoElemental/` dentro de esta raíz Git.
- La plantilla aporta URP, Input System, uGUI/TextMeshPro y AI Navigation. El manifiesto resuelto tiene AI Navigation `2.0.16`.
- Cinemachine `3.1.7` está instalado para el encuadre y seguimiento de cámara.
- `com.unity.pipeline` `0.10.0-exp.1` está instalado por el flujo de creación del Unity CLI para automatización local del Editor; es un paquete experimental y debe tratarse como herramienta de desarrollo.
- La escena actual es todavía la escena inicial de la plantilla. No hay combate implementado ni assets externos integrados.
- El Editor 6.3 está instalado y la licencia Unity Personal está activa. La primera apertura espera que Maximiliano revise y acepte «Unity Editor Software Terms» en la ventana del Editor.
