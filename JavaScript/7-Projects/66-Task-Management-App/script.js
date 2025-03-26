document.addEventListener('DOMContentLoaded',()=>{
  const taskForm = document.getElementById('new-task-form');
  const taskTitle = document.getElementById('task-title');
  const taskDesc = document.getElementById('task-desc');
  const taskDate = document.getElementById('task-date');
  const taskPriority = document.getElementById('task-priority');
  const pendingTasks = document.getElementById('pending-tasks');
  const completedTasks = document.getElementById('completed-tasks');
  const filterPriority = document.getElementById('filter-priority');
  const filterDate = document.getElementById('filter-date');
  const filterStatus = document.getElementById('filter-status');

  const loadTasks=()=>{
    const tasks = JSON.parse(localStorage.getItem('tasks'))||[];
    return tasks;
  };

  const saveTasks = (tasks)=>{
    localStorage.setItem('tasks', JSON.stringify(tasks));
  };

  const renderTasks = () => {
    const tasks = loadTasks();
    pendingTasks.innerHTML = '';
    completedTasks.innerHTML = '';
    tasks.forEach((task) => {
      if (applyFilters(task)) {
        const taskElement = createTaskElement(task);
        if (task.completed) {
          completedTasks.appendChild(taskElement);
        } else {
          pendingTasks.appendChild(taskElement);
        }
      }
    });
  };

  const applyFilters = (task) => {
    const priority = filterPriority.value;
    const date = filterDate.value;
    const status = filterStatus.value;

    if (priority && task.priority !== priority) return false;
    if (date && task.date !== date) return false;
    if (status === 'pending' && task.completed) return false;
    if (status === 'completed' && !task.completed) return false;

    return true;
  };

  const createTaskElement = (task) => {
    const taskDiv = document.createElement('div');
    taskDiv.classList.add('task');
    if (task.completed) taskDiv.classList.add('completed');
    taskDiv.innerHTML = `
      <input type="checkbox" class="complete-task" ${task.completed ? 'checked' : ''}>
      <h3>${task.title}</h3>
      <div id="task-p"><p>${task.desc}</p></div>
      <p class="tasks-dp">Due: ${task.date}</p>
      <p class="tasks-dp">Priority: ${task.priority}</p>
      <button class="edit-task"><i class="fa-solid fa-pen-to-square"></i></button>
      <button class="delete-task"><i class="fa-solid fa-trash-can"></i></button>`;
    taskDiv.querySelector('.delete-task').addEventListener('click', () => {
      deleteTask(task.id);
    });
    taskDiv.querySelector('.complete-task').addEventListener('click', () => {
      toggleCompletion(task.id);
    });
    taskDiv.querySelector('.edit-task').addEventListener('click', () => {
      editTask(task.id);
    });
    return taskDiv;
  };

  const addTask = (task) => {
    const tasks = loadTasks();
    tasks.push(task);
    saveTasks(tasks);
    renderTasks();
  };

  const deleteTask = (id) => {
    const tasks = loadTasks();
    const updatedTasks = tasks.filter((task) => task.id !== id);
    saveTasks(updatedTasks);
    renderTasks();
  };

  const toggleCompletion = (id) => {
    const tasks = loadTasks();
    const updatedTasks = tasks.map((task) => {
      if (task.id === id) {
        task.completed = !task.completed;
      }
      return task;
    });
    saveTasks(updatedTasks);
    renderTasks();
  };

  const editTask = (id) => {
    const tasks = loadTasks();
    const taskToEdit = tasks.find((task) => task.id === id);
    taskTitle.value = taskToEdit.title;
    taskDesc.value = taskToEdit.desc;
    taskDate.value = taskToEdit.date;
    taskPriority.value = taskToEdit.priority;
    deleteTask(id);
  };

  taskForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const newTask = {
      id: Date.now(),
      title: taskTitle.value,
      desc: taskDesc.value,
      date: taskDate.value,
      priority: taskPriority.value,
      completed: false,
    };
    addTask(newTask);
    taskForm.reset();
  });

  filterPriority.addEventListener('change', renderTasks);
  filterDate.addEventListener('change', renderTasks);
  filterStatus.addEventListener('change', renderTasks);

  renderTasks();
});
