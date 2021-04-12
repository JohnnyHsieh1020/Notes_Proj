function delNote(noteId){
    fetch('/delete-note', {
        method: 'POST',
        body: JSON.stringify({ noteId:noteId}),
    }).then((_res) => {
        // Reload the window with GET method
        window.location.href = '/';
    })
}