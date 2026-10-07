import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove all tsParticles script tags
content = re.sub(r'<script src="https://cdn.jsdelivr.net/npm/tsparticles.*?</script>', '', content, flags=re.DOTALL)

# Replace CSS
old_css = r'<style>.*?logo-float \{'
new_css = r'''<style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;700;900&display=swap');
        
        body { 
            background-color: #030303;
            color: #f8fafc; 
            font-family: 'Inter', sans-serif; 
            overflow-x: hidden;
            margin: 0;
        }

        .aurora-bg {
            position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
            background-color: #000;
            overflow: hidden; z-index: 0;
        }
        .aurora-blob {
            position: absolute;
            filter: blur(90px);
            opacity: 0.5;
            animation: drift 25s infinite alternate ease-in-out;
            border-radius: 50%;
        }
        .aurora-1 { width: 50vw; height: 50vw; background: #2563eb; top: -10%; left: -10%; }
        .aurora-2 { width: 45vw; height: 45vw; background: #059669; bottom: -10%; right: -10%; animation-delay: -5s; }
        .aurora-3 { width: 60vw; height: 60vw; background: #7c3aed; top: 20%; left: 20%; animation-delay: -10s; }

        @keyframes drift {
            0% { transform: translate(0, 0) scale(1); }
            50% { transform: translate(5vw, 5vh) scale(1.1); }
            100% { transform: translate(-5vw, -5vh) scale(0.9); }
        }

        .grid-overlay {
            position: fixed; inset: 0; z-index: 1; pointer-events: none;
            background-image: 
                linear-gradient(to right, rgba(255,255,255,0.03) 1px, transparent 1px),
                linear-gradient(to bottom, rgba(255,255,255,0.03) 1px, transparent 1px);
            background-size: 50px 50px;
            mask-image: radial-gradient(circle at center, black, transparent 80%);
            -webkit-mask-image: radial-gradient(circle at center, black, transparent 80%);
        }

        .content-wrapper {
            position: relative;
            z-index: 10;
        }

        #map { position: absolute; inset: 0; width: 100%; height: 100%; border-radius: 1rem; z-index: 1; }
        
        .glass-panel {
            background: rgba(10, 10, 12, 0.3);
            backdrop-filter: blur(30px) saturate(180%);
            -webkit-backdrop-filter: blur(30px) saturate(180%);
            border: 1px solid rgba(255, 255, 255, 0.08);
            box-shadow: 0 20px 40px -10px rgba(0, 0, 0, 0.8);
        }

        .metric-card {
            background: rgba(255, 255, 255, 0.02);
            border: 1px solid rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            transition: all 0.5s cubic-bezier(0.16, 1, 0.3, 1);
            position: relative;
            overflow: hidden;
            border-radius: 1rem;
        }

        .metric-card > * { position: relative; z-index: 1; }

        @media (hover: hover) and (pointer: fine) {
            .metric-card:hover {
                background: rgba(255, 255, 255, 0.05);
                border: 1px solid rgba(255, 255, 255, 0.15);
                transform: translateY(-4px) scale(1.01);
                box-shadow: 0 15px 30px -5px rgba(0,0,0,0.5);
            }
        }

        /* Custom Leaflet popup */
        .leaflet-popup-content-wrapper {
            background: rgba(15, 15, 18, 0.8) !important;
            color: #f8fafc !important;
            border: 1px solid rgba(255, 255, 255, 0.15) !important;
            border-radius: 1rem !important;
            box-shadow: 0 15px 35px -5px rgba(0, 0, 0, 0.9) !important;
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
        }
        .leaflet-popup-tip {
            background: rgba(15, 15, 18, 0.8) !important;
            backdrop-filter: blur(20px);
        }
        .city-marker {
            background-color: #ef4444;
            border-radius: 50%;
            border: 2px solid #ffffff;
            box-shadow: 0 0 15px rgba(239, 68, 68, 0.9);
            animation: pulse 2s infinite cubic-bezier(0.4, 0, 0.6, 1);
        }
        @keyframes pulse {
            0% { box-shadow: 0 0 0 0 rgba(239, 68, 68, 0.8); }
            70% { box-shadow: 0 0 0 20px rgba(239, 68, 68, 0); }
            100% { box-shadow: 0 0 0 0 rgba(239, 68, 68, 0); }
        }

        .leaflet-layer, .leaflet-control-zoom-in, .leaflet-control-zoom-out, .leaflet-control-attribution {
            filter: invert(100%) hue-rotate(180deg) brightness(85%) contrast(95%);
        }

        @media (min-width: 1024px) {
            ::-webkit-scrollbar { width: 6px; }
            ::-webkit-scrollbar-track { background: transparent; }
            ::-webkit-scrollbar-thumb { background: rgba(255, 255, 255, 0.1); border-radius: 10px; }
            ::-webkit-scrollbar-thumb:hover { background: rgba(255, 255, 255, 0.2); }
        }

        .logo-float {'''
content = re.sub(old_css, new_css, content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
