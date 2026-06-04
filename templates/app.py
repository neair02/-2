@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    # Проверка: существует ли задача с таким индексом
    if task_id < 0 or task_id >= len(tasks):
        return "Задача не найдена", 404
    
    task = tasks[task_id]  # получаем словарь задачи
    
    if request.method == 'POST':
        new_text = request.form.get('task', '').strip()
        old_text = task['text']  # запоминаем старый текст
        
        # Проверка на пустое поле
        if new_text == '':
            return render_template('edit.html', task=task, message="Текст не может быть пустым!")
        
        # Проверка: ничего не изменилось
        if new_text == old_text:
            return render_template('edit.html', task=task, message="Ничего не изменено")
        
        # Если всё ок — сохраняем новый текст
        tasks[task_id]['text'] = new_text
        save_tasks(tasks)
        return redirect('/')
    
    # GET-запрос — показываем форму редактирования
    return render_template('edit.html', task=task)
