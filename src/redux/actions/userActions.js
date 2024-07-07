import axios from 'axios';

export const FETCH_USERS_SUCCESS = 'FETCH_USERS_SUCCESS';

export const fetchUsers = () => async (dispatch) => {
  try {
    const response = await axios.get('/users');
    dispatch({
      type: FETCH_USERS_SUCCESS,
      payload: response.data,
    });
  } catch (error) {
    console.error('Error fetching users:', error);
  }
};