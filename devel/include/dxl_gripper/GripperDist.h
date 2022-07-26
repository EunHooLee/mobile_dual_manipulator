// Generated by gencpp from file dxl_gripper/GripperDist.msg
// DO NOT EDIT!


#ifndef DXL_GRIPPER_MESSAGE_GRIPPERDIST_H
#define DXL_GRIPPER_MESSAGE_GRIPPERDIST_H

#include <ros/service_traits.h>


#include <dxl_gripper/GripperDistRequest.h>
#include <dxl_gripper/GripperDistResponse.h>


namespace dxl_gripper
{

struct GripperDist
{

typedef GripperDistRequest Request;
typedef GripperDistResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct GripperDist
} // namespace dxl_gripper


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::dxl_gripper::GripperDist > {
  static const char* value()
  {
    return "47ad84b25c08b18a1fb3684555468caf";
  }

  static const char* value(const ::dxl_gripper::GripperDist&) { return value(); }
};

template<>
struct DataType< ::dxl_gripper::GripperDist > {
  static const char* value()
  {
    return "dxl_gripper/GripperDist";
  }

  static const char* value(const ::dxl_gripper::GripperDist&) { return value(); }
};


// service_traits::MD5Sum< ::dxl_gripper::GripperDistRequest> should match
// service_traits::MD5Sum< ::dxl_gripper::GripperDist >
template<>
struct MD5Sum< ::dxl_gripper::GripperDistRequest>
{
  static const char* value()
  {
    return MD5Sum< ::dxl_gripper::GripperDist >::value();
  }
  static const char* value(const ::dxl_gripper::GripperDistRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::dxl_gripper::GripperDistRequest> should match
// service_traits::DataType< ::dxl_gripper::GripperDist >
template<>
struct DataType< ::dxl_gripper::GripperDistRequest>
{
  static const char* value()
  {
    return DataType< ::dxl_gripper::GripperDist >::value();
  }
  static const char* value(const ::dxl_gripper::GripperDistRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::dxl_gripper::GripperDistResponse> should match
// service_traits::MD5Sum< ::dxl_gripper::GripperDist >
template<>
struct MD5Sum< ::dxl_gripper::GripperDistResponse>
{
  static const char* value()
  {
    return MD5Sum< ::dxl_gripper::GripperDist >::value();
  }
  static const char* value(const ::dxl_gripper::GripperDistResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::dxl_gripper::GripperDistResponse> should match
// service_traits::DataType< ::dxl_gripper::GripperDist >
template<>
struct DataType< ::dxl_gripper::GripperDistResponse>
{
  static const char* value()
  {
    return DataType< ::dxl_gripper::GripperDist >::value();
  }
  static const char* value(const ::dxl_gripper::GripperDistResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // DXL_GRIPPER_MESSAGE_GRIPPERDIST_H
