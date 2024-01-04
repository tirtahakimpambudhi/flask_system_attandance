function formatTimestamp(timestamp) {
    // Create a new Date object
    const date = new Date(timestamp);

    // Define options for toLocaleString
    const options = {
        year: 'numeric',
        month: 'long',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit',
        hour12: false
    };

    // Format the date
    const formattedDate = date.toLocaleString('en-GB', options);
    
    return formattedDate;
}
const showDetails = (name, nis, major,status,time) => {
    document.getElementById('studentName').textContent = name;
    document.getElementById('studentNIS').textContent = nis;
    document.getElementById('studentMajor').textContent = major;
    document.getElementById('studentStatus').textContent = (status == "attend") ?"Hadir" :"Tidak Hadir";
    document.getElementById('studentTime').textContent = formatTimestamp(time);
  }