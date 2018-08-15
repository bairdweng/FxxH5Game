//
//  FxxNetwork.h
//  fxxproject
//
//  Created by  翁献山 on 2018/8/8.
//  Copyright © 2018年  翁献山. All rights reserved.
//

#import <Foundation/Foundation.h>
#import "ZSNetTool.h"
@interface FxxNetwork : NSObject
+ (instancetype)sharedInstance;

/**
注册

 @param appName app名称
 @param bundleidentifier app表示
 @param needURL 未知
 @param view 视图
 @param success 成功回调
 @param failure 失败回调
 */
-(void)Regisdevicebygame:(NSString *)appName
        bundleidentifier:(NSString *)bundleidentifier
                 needURL:(NSString *)needURL
                    view:(UIView *)view
                 success:(void (^)(id data))success
                 failure:(void (^)(NSError *error))failure;


/**
 用户注册

 @param userName 用户账号
 @param passWord 用户密码
 @param success 成功回调
 @param failure 失败回调
 */
-(void)signup:(NSString *)userName
     passWord:(NSString *)passWord
         view:(UIView *)view
      success:(void (^)(id data))success
      failure:(void (^)(NSError *error))failure;

/**
 用户登录
 @param userName 用户账号
 @param passWord 用户密码
 @param success 成功回调
 @param failure 失败回调
 */
-(void)gamelogin:(NSString *)userName
        passWord:(NSString *)passWord
            view:(UIView *)view
         success:(void (^)(id data))success
         failure:(void (^)(NSError *error))failure;

@end
