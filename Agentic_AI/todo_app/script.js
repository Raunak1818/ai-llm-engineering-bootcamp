document.addEventListener("DOMContentLoaded", loadTasks);
function loadTasks(){
    const tasks = JSON.parse(localStorage.getItem("tasks")) || [];
    tasks.forEach(task => renderTask(task.text, task.completed));
}
function addTask(){
    const taskInput = document.getElementById("taskInput");
    const text = taskInput.value.trim();
    if(!text) return;
    renderTask(text, false);
    saveTasks();
    taskInput.value = "";
}
function renderTask(text, completed){
    const list = document.getElementById("taskList");
    const li = document.createElement("li");
    if(completed) li.classList.add("completed");
    const span = document.createElement("span");
    span.textContent = text;
    span.className = "task-text";
    span.onclick = () => {
        li.classList.toggle("completed");
        saveTasks();
    };
    const delBtn = document.createElement("button");
    delBtn.textContent = "Delete";
    delBtn.className = "delete";
    delBtn.onclick = () => {
        li.remove();
        saveTasks();
    };
    li.appendChild(span);
    li.appendChild(delBtn);
    list.appendChild(li);
}
function saveTasks(){
    const list = document.getElementById("taskList");
    const tasks = [];
    list.querySelectorAll("li").forEach(li => {
        tasks.push({
            text: li.querySelector("(.task-text)").textContent,
            completed: li.classList.contains("completed")
        });
    });
    localStorage.setItem("tasks", JSON.stringify(tasks));
}