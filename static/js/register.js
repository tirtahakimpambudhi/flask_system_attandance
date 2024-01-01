  // Fungsi untuk mengonversi data URI menjadi blob
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

  // Fungsi untuk mempersiapkan formulir dengan data foto
  function prepareForm() {
    const dataURL = canvas.toDataURL('image/png');
    const blob = dataURItoBlob(dataURL);
    const file = new File([blob], 'photo.png', { type: 'image/png' });
    const dataTransfer = new DataTransfer();
    dataTransfer.items.add(file);
    document.getElementById('editPhoto').files = dataTransfer.files;
    document.getElementById('editPhoto').disabled = false; // Mengaktifkan input photo
  }

  // Fungsi untuk memvalidasi formulir sebelum pengiriman
  const validateForm = () => {
    const fileInput = document.getElementById('editPhoto');
    if (!fileInput.files.length) {
      Swal.fire({
        icon: 'error',
        title: 'Oops...',
        text: 'You must verify your face before submitting the form.',
      });
      return false;
    }
    return true;
  }

  // Fungsi untuk membuka kamera
  const openCamera = () => {
    const cameraModal = new bootstrap.Modal(document.getElementById('cameraModal'));
    cameraModal.show();
    startCamera();
  }

  // Fungsi untuk memulai kamera
  const startCamera = () => {
    const video = document.getElementById('video');
    if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
      navigator.mediaDevices.getUserMedia({ video: true }).then(stream => {
        video.srcObject = stream;
        video.play();
      });
    }
  }

  // Fungsi untuk mengambil foto dari kamera
  const capturePhoto = () => {
    const video = document.getElementById('video');
    const canvas = document.getElementById('canvas');
    const context = canvas.getContext('2d');
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    context.drawImage(video, 0, 0, video.videoWidth, video.videoHeight);

    const photoData = canvas.toDataURL('image/png');
    verifyFace(photoData);
  }

  // Fungsi untuk memverifikasi wajah dari foto
  const verifyFace = (photoData) => {
    const resultDiv = document.getElementById('verificationResult');

    fetch(VERIFY_URL, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ image: photoData })
    })
    .then(response => response.json())
    .then(data => {
      if (data.verify) {
        resultDiv.innerHTML = '<span class="text-success">Face verified successfully!</span>';
        
        // Set the photo data as the value of the file input
        const blob = dataURItoBlob(photoData);
        const fileInput = document.getElementById('editPhoto');
        const file = new File([blob], "register_face_photo.png", { type: "image/png" });

        const dataTransfer = new DataTransfer();
        dataTransfer.items.add(file);
        fileInput.files = dataTransfer.files;
      } else {
        resultDiv.innerHTML = '<span class="text-danger">No face detected. Please try again.</span>';
      }
    })
    .catch(error => {
      console.error('Error verifying face:', error);
      resultDiv.innerHTML = '<span class="text-danger">An error occurred during verification. Please try again.</span>';
    });


    const cameraModal = bootstrap.Modal.getInstance(document.getElementById('cameraModal'));
    cameraModal.hide();
  }