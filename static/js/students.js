const showDetails = (name, nis, attendanceNumber, major,yearGraduated,src) => {
    document.getElementById('studentName').textContent = name;
    document.getElementById('studentNIS').textContent = nis;
    document.getElementById('studentAttendanceNumber').textContent = attendanceNumber;
    document.getElementById('studentMajor').textContent = major;
    document.getElementById('studentYear').textContent = yearGraduated;
    document.getElementById('studentPhoto').src = src;
  }

const prepareEdit = (id,name, nis, attendanceNumber, major,yearGraduated, photoUrl) => {
    document.getElementById('editName').value = name;
    document.getElementById('editNIS').value = nis;
    document.getElementById('editAttendanceNumber').value = attendanceNumber;
    document.getElementById('editYearGradueated').value = yearGraduated;
        // Mengambil elemen select
        const editMajorSelect = document.getElementById('major');

        // Membuat array opsi major
        const majorOptions = ["SIJA", "DKV", "MM", "TKJ", "TITL", "TAV", "TKR", "TP", "KGSP", "GEOMATIKA"];
    
        // Menghapus opsi sebelumnya (jika ada)
        editMajorSelect.innerHTML = "";
    
        // Membuat opsi baru dan menambahkannya ke dalam dropdown
        majorOptions.forEach(option => {
            const optionElement = document.createElement("option");
            optionElement.value = option;
            optionElement.textContent = option;
            if (option === major) {
                optionElement.selected = true;
            }
            editMajorSelect.appendChild(optionElement);
        });
    
    document.getElementById('editForm').setAttribute("action",`${document.getElementById('editForm').getAttribute("action")}/${id}`);
}

const openCamera = () => {
  const cameraModal = new bootstrap.Modal(document.getElementById('cameraModal'));
  cameraModal.show();
  startCamera();
}

const startCamera = () => {
  const video = document.getElementById('video');
  if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
    navigator.mediaDevices.getUserMedia({ video: true }).then(stream => {
      video.srcObject = stream;
      video.play();
    });
  }
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






function showError(message) {
  Swal.fire({
      icon: "error",
      title: "Error",
      text: message
  });
}