
  const capturePhoto = () => {
    const video = document.getElementById('video');
    const canvas = document.getElementById('canvas');
    const context = canvas.getContext('2d');
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    context.drawImage(video, 0, 0, video.videoWidth, video.videoHeight);

    verifyFace(canvas.toDataURL('image/png'),VERIFY_URL);
  }

  const verifyPhoto = () => {
    const id = document.getElementById("editForm").getAttribute("action").split("/").at(-1);
    const video = document.getElementById('video');
    const canvas = document.getElementById('canvas');
    const context = canvas.getContext('2d');
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    context.drawImage(video, 0, 0, video.videoWidth, video.videoHeight);

    verifyFace(canvas.toDataURL('image/png'),MATCH_ID_URL(id));
  }
  const verifyFace = (photoData,url) => {
    fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ image: photoData })
    })
    .then(response => response.json())
    .then(data => {
      if (data.match || data.verify) {
        Swal.fire({
          position: "top-center",
          icon: "success",
          title: data.message,
          showConfirmButton: false,
          timer: 1500
        });     
        // Set the photo data as the value of the file input
        const blob = dataURItoBlob(photoData);
        const fileInput = document.getElementById('editPhoto');
        const file = new File([blob], "edit_face_photo.png", { type: "image/png" });

        const dataTransfer = new DataTransfer();
        dataTransfer.items.add(file);
        fileInput.files = dataTransfer.files;
      } else {
        Swal.fire({
          icon: "error",
          title: "Oops...",
          text: data.message,
        });
      }
    })
    .catch(error => {
      showError(error);
    });


    const cameraModal = bootstrap.Modal.getInstance(document.getElementById('cameraModal'));
    cameraModal.hide();
  }
  function saveChange(event) {
    event.preventDefault();
    openCamera();
    document.getElementById("buttonCapture").setAttribute("onclick","verifyPhoto();");
    document.getElementById("buttonCapture").addEventListener("mouseup",() => {
      const form = document.getElementById('editForm');
      const url = form.action;
      const formData = new FormData(form);
      const jsonData = {};
  
      formData.forEach((value, key) => {
        jsonData[key] = value;
      });
  
      const fileInput = document.getElementById('editPhoto');
      const file = fileInput.files[0];
  
      if (file) {
        const reader = new FileReader();
        reader.onload = function(event) {
          jsonData["image"] = event.target.result;
  
          const id = form.getAttribute("action").split("/").at(-1);
          fetch(EDIT_URL(id), {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify(jsonData)
          })
          .then(response => response.json())
          .then(data => {
            console.log(data);
            if (data.status == "success") {
              Swal.fire({
                icon: "success",
                title: data.status,
                text: data.message
              })
              window.location.reload();
            } else {
              Swal.fire({
                icon: "error",
                title: data.status,
                text: data.message
              });
            }
          })
          .catch(error => {
            showError(error);
          });
        };
        reader.readAsDataURL(file);
      } else {
        const id = form.getAttribute("action").split("/").at(-1);
        fetch(EDIT_URL(id), {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(jsonData)
        })
        .then(response => response.json())
        .then(data => {
          console.log(data);
          if (data.status == "success") {
            Swal.fire({
              icon: "success",
              title: "Success",
              text: data.message
            }).then(() => {
              window.location.reload();
            });
          } else {
            Swal.fire({
              icon: "error",
              title: "Error",
              text: data.message
            });
          }
        })
        .catch(error => {
          showError(error);
        });
      }
    });
  }
