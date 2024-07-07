import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { fetchTasks } from '../redux/actions/taskActions';
import { io } from 'socket.io-client';

const TaskList = () => {
  const dispatch = useDispatch();
  const tasks = useSelector((state) => state.tasks);

  useEffect(() => {
    dispatch(fetchTasks());

    const socket = io('http://localhost:5000');
    socket.on('update_task', (updatedTask) => {
      dispatch(fetchTasks()); // Refetch tasks on update
    });

    return () => {
      socket.disconnect();
    };
  }, [dispatch]);

  return (
    <div>
      <h1>Tasks</h1>
      <ul>
        {tasks.map((task) => (
          <li key={task.id}>{task.name}</li>
        ))}
      </ul>
    </div>
  );
};

export default TaskList;