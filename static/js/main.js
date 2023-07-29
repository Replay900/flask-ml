document.getElementById("uploadForm").onsubmit = function (event) {
    event.preventDefault();
    const formData = new FormData();
    formData.append("file", document.getElementById("fileInput").files[0]);

    fetch("/upload", {
        method: "POST",
        body: formData,
    })
    .then((response) => response.json())
    .then((data) => {
        document.getElementById("result").innerHTML = data.result;
    })
    .catch((error) => console.error("Error:", error));
};