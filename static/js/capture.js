
    let video;
    let canvas;
    let photoInput;

    function init() {
        video = document.getElementById('video');
        canvas = document.getElementById('canvas');
        photoInput = document.getElementById('photo');

        navigator.mediaDevices.getUserMedia({ video: true })
            .then(stream => {
                video.srcObject = stream;
            })
            .catch(error => {
                console.error('Error accessing webcam:', error);
                alert('Tidak dapat mengakses webcam. Pastikan Anda memberikan izin untuk mengakses kamera.');
            });
    }

    function capture() {
        const context = canvas.getContext('2d');
        context.drawImage(video, 0, 0, canvas.width, canvas.height);
        const dataURL = canvas.toDataURL('image/png');
        photoInput.value = dataURL;
        canvas.style.display = 'block';
        video.style.display = 'none';
    }

    function dataURItoBlob(dataURI) {
        const byteString = atob(dataURI.split(',')[1]);
        const mimeString = dataURI.split(',')[0].split(':')[1].split(';')[0];
        const ab = new ArrayBuffer(byteString.length);
        const ia = new Uint8Array(ab);
        for (let i = 0; i < byteString.length; i++) {
            ia[i] = byteString.charCodeAt(i);
        }
        return new Blob([ab], { type: mimeString });
    }

    function prepareForm() {
        const dataURL = canvas.toDataURL('image/png');
        const blob = dataURItoBlob(dataURL);
        const file = new File([blob], 'photo.png', { type: 'image/png' });
        const dataTransfer = new DataTransfer();
        dataTransfer.items.add(file);
        document.getElementById('photo').files = dataTransfer.files;
    }

    init();