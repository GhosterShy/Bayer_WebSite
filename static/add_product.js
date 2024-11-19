// const fileInput = document.getElementById('file-upload');
// const fileName = document.getElementById('file-name');
// const dropZone = document.getElementById('drop-zone');

// // Функция для отображения имени выбранного файла
// function showFileName(event) {
//     const files = event.target.files || event.dataTransfer.files;
//     if (files.length > 0) {
//         fileName.textContent = files[0].name;
//     } else {
//         fileName.textContent = "Файл не выбран";
//     }
// }

// // Обработка событий drag-and-drop
// dropZone.addEventListener('dragover', (event) => {
//     event.preventDefault();
//     dropZone.classList.add('hover');
// });

// dropZone.addEventListener('dragleave', () => {
//     dropZone.classList.remove('hover');
// });

// dropZone.addEventListener('drop', (event) => {
//     event.preventDefault();
//     dropZone.classList.remove('hover');
//     const files = event.dataTransfer.files;
//     if (files.length > 0) {
//         fileInput.files = files; // Устанавливаем файлы в input
//         showFileName(event); // Показываем имя файла
//     }
// });

// // Клик по зоне вызывает выбор файла
// dropZone.addEventListener('click', () => {
//     fileInput.click();
// });

//     // Функция для обработки ссылки на файл
//     function handleLink() {
//         const link = document.getElementById('file-link').value;
//         const fileName = document.getElementById('file-name');
//         if (link) {
//             fileName.textContent = `Загружается файл по ссылке: ${link}`;
//             console.log("Ссылка на файл:", link);
//         }
//     }



const fileInput = document.getElementById('file-upload');
                const fileName = document.getElementById('file-name');
                const dropZone = document.getElementById('drop-zone');
        
                // Функция для отображения имени выбранного файла
                function showFileName(event) {
                    const files = event.target.files || event.dataTransfer.files;
                    if (files.length > 0) {
                        fileName.textContent = `Выбран файл: ${files[0].name}`;
                    } else {
                        fileName.textContent = "Файл не выбран";
                    }
                }
        
                // Обработка событий drag-and-drop
                dropZone.addEventListener('dragover', (event) => {
                    event.preventDefault();
                    dropZone.classList.add('hover');
                });
        
                dropZone.addEventListener('dragleave', () => {
                    dropZone.classList.remove('hover');
                });
        
                dropZone.addEventListener('drop', (event) => {
                    event.preventDefault();
                    dropZone.classList.remove('hover');
                    const files = event.dataTransfer.files;
                    if (files.length > 0) {
                        fileInput.files = files; // Устанавливаем файлы в input
                        showFileName(event); // Показываем имя файла
                    }
                });
        
                // Клик по зоне вызывает выбор файла
                dropZone.addEventListener('click', () => {
                    fileInput.click();
                });
        
                // Функция для обработки ссылки на файл
                function handleLink() {
                    const link = document.getElementById('file-link').value;
                    if (link) {
                        fileName.textContent = `Загружается файл по ссылке: ${link}`;
                        console.log("Ссылка на файл:", link);
                    } else {
                        alert("Пожалуйста, введите корректную ссылку.");
                    }
                }