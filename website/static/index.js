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
      window.location.href = "/car-color";
    });
  }

  function deleteModel(modelId) {
    fetch("/delete-model", {
      method: "POST",
      body: JSON.stringify({ modelId: modelId }),
    }).then((_res) => {
      window.location.href = "/car-model";
    });
  }