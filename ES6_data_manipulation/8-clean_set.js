export default function cleanSet(set, startString) {
  let result = '';

  if (!startString || typeof startString !== 'string') {
    return '';
  }

  for (const item of set) {
    if (item.startsWith(startString)) {
      result += `${item.substring(startString.length)}-`;
    }
  }

  return result.slice(0, -1);
}
