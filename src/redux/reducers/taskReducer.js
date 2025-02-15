import { FETCH_TASKS_SUCCESS } from '../actions/taskActions';

const taskReducer = (state = [], action) => {
  switch (action.type) {
    case FETCH_TASKS_SUCCESS:
      return action.payload;
    default:
      return state;
  }
};

export default taskReducer;