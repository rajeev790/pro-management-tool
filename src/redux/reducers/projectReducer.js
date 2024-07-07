import { FETCH_PROJECTS_SUCCESS } from '../actions/projectActions';

const projectReducer = (state = [], action) => {
  switch (action.type) {
    case FETCH_PROJECTS_SUCCESS:
      return action.payload;
    default:
      return state;
  }
};

export default projectReducer;