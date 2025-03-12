import ClassRoom from './0-classroom';

const initializeRooms = () => {
  const maxSize = [19, 20, 34];
  return maxSize.map((size) => new ClassRoom(size));
};

export default initializeRooms;
