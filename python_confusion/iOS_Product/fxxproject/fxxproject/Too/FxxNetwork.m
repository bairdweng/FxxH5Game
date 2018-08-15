//
//  FxxNetwork.m
//  fxxproject
//
//  Created by  翁献山 on 2018/8/8.
//  Copyright © 2018年  翁献山. All rights reserved.
//

#import "FxxNetwork.h"
#import "NSDictionary+safeGet.h"
@implementation FxxNetwork
+ (instancetype)sharedInstance {
    static dispatch_once_t onceToken;
    static id instance;
    dispatch_once(&onceToken, ^{
        instance = [[self alloc]init];
    });
    return instance;
}
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
                 failure:(void (^)(NSError *error))failure {
    
    NSDictionary *Par =@{@"appName":appName,@"bundleIdentifier":bundleidentifier,@"needURL":needURL};
    
    [[ZSNetTool sharedInstance]POST:[NSString stringWithFormat:@"%@/regisdevicebygame",addressurl]
                         parameters:Par
                               view:view
                            success:^(id responseObject)
    {
        if (success) {
            success(responseObject);
        }
    } failure:^(NSError *error) {
        
    }];
    
}

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
      failure:(void (^)(NSError *error))failure{
    
    NSDictionary *Par =@{@"userName":userName,@"passWord":passWord};
    
    [[ZSNetTool sharedInstance]POST:[NSString stringWithFormat:@"%@/signup",addressurl]
                         parameters:Par
                               view:view
                            success:^(id responseObject)
     {
         if ([responseObject jh_objectForKey:@"error"]) {
             [MBProgressHUD showError:[responseObject jh_objectForKey:@"error"] toView:view];
             return ;
         }
         if (success) {
             success(responseObject);
         }
     } failure:^(NSError *error) {
         
     }];
}
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
         failure:(void (^)(NSError *error))failure{
    
    NSDictionary *Par =@{@"userName":userName,@"passWord":passWord};
    
    [[ZSNetTool sharedInstance]POST:[NSString stringWithFormat:@"%@/gamelogin",addressurl]
                         parameters:Par
                               view:view
                            success:^(id responseObject)
     {
         if ([responseObject jh_objectForKey:@"error"]) {
             [MBProgressHUD showError:[responseObject jh_objectForKey:@"error"] toView:view];
             return ;
         }
         if (success) {
             success(responseObject);
         }
     } failure:^(NSError *error) {
         
     }];
}

@end
