// Auto-generated. Do not edit!

// (in-package mservo_msg.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let traj_1d = require('./traj_1d.js');

//-----------------------------------------------------------

class traj_2d {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.traj_2d = null;
    }
    else {
      if (initObj.hasOwnProperty('traj_2d')) {
        this.traj_2d = initObj.traj_2d
      }
      else {
        this.traj_2d = new Array(50).fill(new traj_1d());
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type traj_2d
    // Check that the constant length array field [traj_2d] has the right length
    if (obj.traj_2d.length !== 50) {
      throw new Error('Unable to serialize array field traj_2d - length must be 50')
    }
    // Serialize message field [traj_2d]
    obj.traj_2d.forEach((val) => {
      bufferOffset = traj_1d.serialize(val, buffer, bufferOffset);
    });
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type traj_2d
    let len;
    let data = new traj_2d(null);
    // Deserialize message field [traj_2d]
    len = 50;
    data.traj_2d = new Array(len);
    for (let i = 0; i < len; ++i) {
      data.traj_2d[i] = traj_1d.deserialize(buffer, bufferOffset)
    }
    return data;
  }

  static getMessageSize(object) {
    return 56;
  }

  static datatype() {
    // Returns string type for a message object
    return 'mservo_msg/traj_2d';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '1e758c7f7f248e577c2b0cf954d10ea6';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    traj_1d[50] traj_2d
    
    ================================================================================
    MSG: mservo_msg/traj_1d
    float64[7] traj
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new traj_2d(null);
    if (msg.traj_2d !== undefined) {
      resolved.traj_2d = new Array(50)
      for (let i = 0; i < resolved.traj_2d.length; ++i) {
        if (msg.traj_2d.length > i) {
          resolved.traj_2d[i] = traj_1d.Resolve(msg.traj_2d[i]);
        }
        else {
          resolved.traj_2d[i] = new traj_1d();
        }
      }
    }
    else {
      resolved.traj_2d = new Array(50).fill(new traj_1d())
    }

    return resolved;
    }
};

module.exports = traj_2d;
