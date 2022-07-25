// Generated by gencpp from file dxl_gripper/GripperDistResponse.msg
// DO NOT EDIT!


#ifndef DXL_GRIPPER_MESSAGE_GRIPPERDISTRESPONSE_H
#define DXL_GRIPPER_MESSAGE_GRIPPERDISTRESPONSE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace dxl_gripper
{
template <class ContainerAllocator>
struct GripperDistResponse_
{
  typedef GripperDistResponse_<ContainerAllocator> Type;

  GripperDistResponse_()
    : result(false)  {
    }
  GripperDistResponse_(const ContainerAllocator& _alloc)
    : result(false)  {
  (void)_alloc;
    }



   typedef uint8_t _result_type;
  _result_type result;





  typedef boost::shared_ptr< ::dxl_gripper::GripperDistResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::dxl_gripper::GripperDistResponse_<ContainerAllocator> const> ConstPtr;

}; // struct GripperDistResponse_

typedef ::dxl_gripper::GripperDistResponse_<std::allocator<void> > GripperDistResponse;

typedef boost::shared_ptr< ::dxl_gripper::GripperDistResponse > GripperDistResponsePtr;
typedef boost::shared_ptr< ::dxl_gripper::GripperDistResponse const> GripperDistResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::dxl_gripper::GripperDistResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::dxl_gripper::GripperDistResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::dxl_gripper::GripperDistResponse_<ContainerAllocator1> & lhs, const ::dxl_gripper::GripperDistResponse_<ContainerAllocator2> & rhs)
{
  return lhs.result == rhs.result;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::dxl_gripper::GripperDistResponse_<ContainerAllocator1> & lhs, const ::dxl_gripper::GripperDistResponse_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace dxl_gripper

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::dxl_gripper::GripperDistResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::dxl_gripper::GripperDistResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::dxl_gripper::GripperDistResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::dxl_gripper::GripperDistResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::dxl_gripper::GripperDistResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::dxl_gripper::GripperDistResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::dxl_gripper::GripperDistResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "eb13ac1f1354ccecb7941ee8fa2192e8";
  }

  static const char* value(const ::dxl_gripper::GripperDistResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xeb13ac1f1354ccecULL;
  static const uint64_t static_value2 = 0xb7941ee8fa2192e8ULL;
};

template<class ContainerAllocator>
struct DataType< ::dxl_gripper::GripperDistResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "dxl_gripper/GripperDistResponse";
  }

  static const char* value(const ::dxl_gripper::GripperDistResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::dxl_gripper::GripperDistResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "bool result\n"
"\n"
;
  }

  static const char* value(const ::dxl_gripper::GripperDistResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::dxl_gripper::GripperDistResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.result);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct GripperDistResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::dxl_gripper::GripperDistResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::dxl_gripper::GripperDistResponse_<ContainerAllocator>& v)
  {
    s << indent << "result: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.result);
  }
};

} // namespace message_operations
} // namespace ros

#endif // DXL_GRIPPER_MESSAGE_GRIPPERDISTRESPONSE_H
