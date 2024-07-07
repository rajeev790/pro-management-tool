import axios from 'axios';

export const FETCH_PROJECTS_SUCCESS = 'FETCH_PROJECTS_SUCCESS';

export const fetchProjects = () => async (dispatch) => {
  try {
    const response = await axios.get('/projects');
    dispatch({
      type: FETCH_PROJECTS_SUCCESS,
      payload: response.data,
    });
  } catch (error) {
    console.error('Error fetching projects:', error);
  }
};