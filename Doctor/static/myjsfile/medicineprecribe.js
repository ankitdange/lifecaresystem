var selectedRow = null

function onFormSubmit() {
    if (validate()) {
        var formData = readFormData();
        if (selectedRow == null)
            insertNewRecord(formData);
        else
            updateRecord(formData);
        resetForm();
    }
}

function readFormData() {
    var formData = {};
    formData["med"] = document.getElementById("med").value;
    formData["qty"] = document.getElementById("qty").value;
    formData["morningdoes"] = document.getElementById("morningdoes").value;
    formData["afternoondoes"] = document.getElementById("afternoondoes").value;
    formData["eveningdoes"] = document.getElementById("eveningdoes").value;
    return formData;
}

function insertNewRecord(data) {
    var table = document.getElementById("employeeList").getElementsByTagName('tbody')[0];
    var newRow = table.insertRow(table.length);
    cell1 = newRow.insertCell(0);
    cell1.innerHTML = data.med;
    cell2 = newRow.insertCell(1);
    cell2.innerHTML = data.qty;
    cell3 = newRow.insertCell(2);
    cell3.innerHTML = data.morningdoes;
    cell4 = newRow.insertCell(3);
    cell4.innerHTML = data.afternoondoes;
    cell5 = newRow.insertCell(4);
    cell5.innerHTML = data.eveningdoes;
    cell5 = newRow.insertCell(5);
    cell5.innerHTML = `<a onClick="onEdit(this)">Edit</a>
                       <a onClick="onDelete(this)">Delete</a>`;
}

function resetForm() {
    document.getElementById("med").value = "";
    document.getElementById("qty").value = "";
    document.getElementById("morningdoes").value = "";
    document.getElementById("afternoondoes").value = "";
    document.getElementById("eveningdoes").value = "";
    selectedRow = null;
}

function onEdit(td) {
    selectedRow = td.parentElement.parentElement;
    document.getElementById("med").value = selectedRow.cells[0].innerHTML;
    document.getElementById("qty").value = selectedRow.cells[1].innerHTML;
    document.getElementById("morningdoes").value = selectedRow.cells[2].innerHTML;
    document.getElementById("afternoondoes").value = selectedRow.cells[3].innerHTML;
    document.getElementById("eveningdoes").value = selectedRow.cells[4].innerHTML;
}
function updateRecord(formData) {
    selectedRow.cells[0].innerHTML = formData.med;
    selectedRow.cells[1].innerHTML = formData.qty;
    selectedRow.cells[2].innerHTML = formData.morningdoes;
    selectedRow.cells[3].innerHTML = formData.afternoondoes;
    selectedRow.cells[4].innerHTML = formData.eveningdoes;
}

function onDelete(td) {
    if (confirm('Are you sure to delete this record ?')) {
        row = td.parentElement.parentElement;
        document.getElementById("employeeList").deleteRow(row.rowIndex);
        resetForm();
    }
}
function validate() {
    isValid = true;
    if (document.getElementById("med").value == "") {
        isValid = false;
        document.getElementById("fullNameValidationError").classList.remove("hide");
    } else {
        isValid = true;
        if (!document.getElementById("fullNameValidationError").classList.contains("hide"))
            document.getElementById("fullNameValidationError").classList.add("hide");
    }
    return isValid;
}



