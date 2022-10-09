function deleteNote(noteId) {
    fetch("/delete-note", {
      method: "POST",
      body: JSON.stringify({ noteId: noteId }),
    }).then((_res) => {
      window.location.href = "/";
    });
  }


function deleteColor(colorId) {
    fetch("/delete-color", {
      method: "POST",
      body: JSON.stringify({ colorId: colorId }),
    }).then((_res) => {
      window.location.href = "/";
    });
  }