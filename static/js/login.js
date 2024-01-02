var toastElList = [].slice.call(document.querySelectorAll('.toast'))
var toastList = toastElList.map(function (toastEl) {
  return new bootstrap.Toast(toastEl)
})
toastList.forEach(toast => toast.show())

function setActiveButton(buttonId) {
  var buttons = document.querySelectorAll('.btn'); // dapatkan semua button
  buttons.forEach(function(button) {
    if (button.id === buttonId) {
      button.classList.add('active-btn'); // tambahkan kelas untuk warna latar belakang aktif
    } else {
      button.classList.remove('active-btn'); // hapus kelas jika bukan button yang diklik
    }
  });
}

// terapkan fungsi pada event click button
document.getElementById('btn-face-recognition').addEventListener('click', function () {
  setActiveButton('btn-face-recognition');
  var carousel = new bootstrap.Carousel(document.getElementById('login-slider'));
  carousel.to(0); // Go to the first slide (Face Recognition)
});

document.getElementById('btn-form-login').addEventListener('click', function () {
  setActiveButton('btn-form-login');
  var carousel = new bootstrap.Carousel(document.getElementById('login-slider'));
  carousel.to(1); // Go to the second slide (Form Login)
});


const video = document.getElementById('video');
const canvas = document.getElementById('canvas');
const context = canvas.getContext('2d');

// Access the webcam
navigator.mediaDevices.getUserMedia({ video: true })
  .then(stream => {
    video.srcObject = stream;
  })
  .catch(err => {
    console.error("Error accessing the webcam: ", err);
  });

  function capturePhoto() {

    // Draw the current frame from the video on the canvas
    context.drawImage(video, 0, 0, canvas.width, canvas.height);

    // Convert the canvas image to a data URL
    const dataURL = canvas.toDataURL('image/png');

    // Convert data URL to Blob
    const byteString = atob(dataURL.split(',')[1]);
    const mimeString = dataURL.split(',')[0].split(':')[1].split(';')[0];
    const ab = new ArrayBuffer(byteString.length);
    const ia = new Uint8Array(ab);
    for (let i = 0; i < byteString.length; i++) {
      ia[i] = byteString.charCodeAt(i);
    }
    const blob = new Blob([ab], { type: mimeString });

    // Prepare form data
    const formData = new FormData();
    formData.append('photo', blob, 'capture.png');

    // Send the form data to the server
    fetch(ABSEN_MATCH_URL, {
      method: 'POST',
      body: formData
    })
    .then(response => response.json())
    .then(data => {
      if (data.match) {
        Swal.fire({
          position: "top-center",
          icon: "success",
          title: data.message,
          showConfirmButton: false,
          timer: 1500
        });   
        window.location.replace(ABSEN_INDEX);
      } else {
        showError(data.message,LOGIN_URL);
      }
    })
    .catch(error => {
      showError(error,LOGIN_URL);
    });
  }
function showError(message,reload_path) {
  Swal.fire({
    icon: "error",
    title: "Error",
    text: message,
    footer : `a href="${reload_path}">Try Again</a>`
});
}