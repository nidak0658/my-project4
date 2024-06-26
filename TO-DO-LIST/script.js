document.addEventListener('DOMContentLoaded', () => {
    const taskForm = document.getElementById('taskForm');
    const taskInput = document.getElementById('taskInput');
    const taskList = document.getElementById('taskList');

    taskForm.addEventListener('submit', function(event) {
        event.preventDefault();
        addTask(taskInput.value);
        taskInput.value = '';
    });

    function addTask(task) {
        const listItem = document.createElement('li');
        listItem.innerHTML = `
            <span>${task}</span>
            <div>
                <button class="complete-btn">Complete</button>
                <button class="delete-btn">Delete</button>
            </div>
        `;
        taskList.appendChild(listItem);

        const completeBtn = listItem.querySelector('.complete-btn');
        const deleteBtn = listItem.querySelector('.delete-btn');

        completeBtn.addEventListener('click', () => {
            listItem.classList.toggle('completed');
        });

        deleteBtn.addEventListener('click', () => {
            taskList.removeChild(listItem);
        });
    }
});
