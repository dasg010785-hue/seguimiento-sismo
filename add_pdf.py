import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add html2pdf CDN
if 'html2pdf' not in content:
    content = content.replace('</title>', '</title>\n    <script src="https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js"></script>')

# 2. Add PDF Button
old_header_right = r'''<div class="w-full lg:w-auto text-center lg:text-right bg-neutral-800/40 p-2 sm:p-3 rounded-xl border border-neutral-600/30 shadow-lg backdrop-blur-md transform hover:scale-105 transition-all duration-300">
                <p class="font-bold text-xl sm:text-2xl text-white drop-shadow-md" id="selected-city-title">Colombia \(Total\)</p>
                <p class="text-xs sm:text-sm text-emerald-400 font-medium animate-pulse"><i class="fa-solid fa-location-dot mr-1"></i>Seleccione una ciudad</p>
            </div>'''

new_header_right = r'''<div class="w-full lg:w-auto flex flex-row items-center justify-center lg:justify-end gap-3 sm:gap-4">
                <div class="flex-1 lg:flex-none text-center lg:text-right bg-neutral-800/40 p-2 sm:p-3 rounded-xl border border-neutral-600/30 shadow-lg backdrop-blur-md transform hover:scale-105 transition-all duration-300">
                    <p class="font-bold text-xl sm:text-2xl text-white drop-shadow-md" id="selected-city-title">Colombia (Total)</p>
                    <p class="text-xs sm:text-sm text-emerald-400 font-medium animate-pulse"><i class="fa-solid fa-location-dot mr-1"></i>Seleccione una ciudad</p>
                </div>
                <button id="btn-pdf" class="bg-red-600/80 hover:bg-red-500 text-white p-2 sm:p-3 rounded-xl border border-red-400/50 shadow-[0_0_15px_rgba(220,38,38,0.4)] flex flex-col items-center justify-center gap-1 transition-all hover:scale-105 active:scale-95 group">
                    <i class="fa-solid fa-file-pdf text-xl sm:text-2xl group-hover:-translate-y-1 transition-transform"></i>
                    <span class="text-[9px] sm:text-[10px] font-bold uppercase tracking-wider">Informe</span>
                </button>
            </div>'''

content = re.sub(old_header_right, new_header_right, content)

# 3. Add JS for PDF generation
pdf_js = r'''
        // Lógica de PDF
        document.getElementById('btn-pdf').addEventListener('click', function() {
            const btnPdf = this;
            const originalIcon = btnPdf.innerHTML;
            btnPdf.innerHTML = '<i class="fa-solid fa-spinner fa-spin text-xl sm:text-2xl"></i><span class="text-[9px] sm:text-[10px] font-bold uppercase tracking-wider">Espere</span>';
            
            // Ocultar elementos que no queremos en el PDF o ajustar estilos
            const btnReset = document.getElementById('btn-reset');
            if(btnReset) btnReset.style.display = 'none';

            const element = document.querySelector('.content-wrapper');
            const city = document.getElementById('selected-city-title').textContent.trim();
            const filename = `Informe_Sismo_${city.replace(/[^a-z0-9]/gi, '_')}.pdf`;

            const opt = {
                margin:       0.2,
                filename:     filename,
                image:        { type: 'jpeg', quality: 0.98 },
                html2canvas:  { scale: 2, useCORS: true, logging: false, backgroundColor: '#030303' },
                jsPDF:        { unit: 'in', format: 'a3', orientation: 'landscape' }
            };

            html2pdf().set(opt).from(element).save().then(() => {
                btnPdf.innerHTML = originalIcon;
                if(btnReset && city !== 'Colombia (Total)') btnReset.style.display = 'flex';
            });
        });
        
        // Recalcular tamaño del mapa al rotar pantalla en móviles'''

content = content.replace('// Recalcular tamaño del mapa al rotar pantalla en móviles', pdf_js)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
