document.getElementById('text-to-image-form').addEventListener('submit', async function (e) {
    e.preventDefault();
    const text = document.getElementById('text').value;

    const response = await fetch('http://127.0.0.1:8000/generate-image', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text })
    });

    if (response.ok) {
        const data = await response.json();
        document.getElementById('generated-image').src = data.image_url;
    } else {
        alert('Error generating image');
    }
});
