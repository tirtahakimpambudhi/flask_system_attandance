  const searchForm = document.getElementById('searchForm');
  const searchInput = document.getElementById('searchInput');
  
  // Melakukan fetch request ketika form pencarian dikirim
  searchForm.addEventListener('submit', function(event) {
    event.preventDefault(); // Mencegah pengiriman formulir
  
    const inputValue = searchInput.value.trim(); // Mendapatkan nilai input dan menghapus spasi di awal dan akhir
    if (inputValue !== '') { // Pastikan nilai input tidak kosong
        const url = SHOW_URL(inputValue); // Membuat URL dengan nilai input
  
        // Melakukan fetch request
        fetch(url)
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                console.log(data);
                // Menghapus isi tabel sebelum menambahkan data baru
                const tbody = document.querySelector('tbody');
                tbody.innerHTML = '';
  
                // Check if data contains 'students' property
                if (data.students && Array.isArray(data.students)) {
                    if (data.students.length > 0) {
                        // Iterasi melalui data dan menambahkannya ke tabel
                        data.students.forEach((student, index) => {
                          
                            const row = `<tr>
                                <th scope="row">${index + 1}</th>
                                <td>${student.name}</td>
                                <td>${student.nis}</td>
                                <td>${student.number_absence}</td>
                                <td>${student.major}</td>
                                <td>
                                    <button class="btn btn-info" style="background-color: #1977cc; color: white;" data-bs-toggle="modal" data-bs-target="#detailModal" onclick="showDetails('${student.name}', '${student.nis}', '${student.number_absence}', '${student.major}', '${student.year_graduated}', '${UPLOAD_FILEPATH(student.id)}')">Detail</button>
                                    <button class="btn btn-warning" data-bs-toggle="modal" data-bs-target="#editModal" onclick="prepareEdit('${student.id}', '${student.name}', '${student.nis}', '${student.number_absence}', '${student.major}', '${student.year_graduated}', '${UPLOAD_FILEPATH(student.id)}')">Edit</button>
                                </td>
                            </tr>`;
                            tbody.insertAdjacentHTML('beforeend', row);
                        });
                    } else {
                        // Display a message when no data is found
                        const row = `<tr>
                            <td colspan="6" class="text-center">No data found for "${inputValue}"</td>
                        </tr>`;
                        tbody.insertAdjacentHTML('beforeend', row);
                    }
                } else {
                    showError(`The data format is incorrect: ${data}`);
                }
            })
            .catch(error => {
                showError(`There was a problem with the fetch operation: ${error}`);
            });
    }
  });  
