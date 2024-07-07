import axios from 'axios';

export const FETCH_TASKS_SUCCESS = 'FETCH_TASKS_SUCCESS';

export const fetchTasks = () => async (dispatch) => {
  try {
    const response = await axios.get('/tasks');
    dispatch({
      type: FETCH_TASKS_SUCCESS,
      payload: response.data,
    });
  } catch (error) {
    console.error('Error fetching tasks:', error);
  }
};