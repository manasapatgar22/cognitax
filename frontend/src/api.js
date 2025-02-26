const API_URL = "http://127.0.0.1:5000";

export async function uploadFile(file) {
    const formData = new FormData();
    formData.append("file", file);

    const response = await fetch(`${API_URL}/upload`, {
        method: "POST",
        body: formData,
    });

    return response.json();
}
