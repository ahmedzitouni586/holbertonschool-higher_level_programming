#!/usr/bin/node
exports.esrever = function (list) {
  let tmp;
  for (let start = 0, end = list.length - 1; start < end; ++start, --end) {
    tmp = list[start];
    list[start] = list[end];
    list[end] = tmp;
  }
  return (list);
};
