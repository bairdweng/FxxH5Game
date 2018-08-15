//
//  RegViewModel.h
//  fxxproject
//
//  Created by  翁献山 on 2018/8/6.
//  Copyright © 2018年  翁献山. All rights reserved.
//

#import <Foundation/Foundation.h>
#import "RegViewController.h"
@interface RegViewModel : NSObject


/**
 注册按钮样式

 @param Vc 当前视图控制器
 @return 当前viewmodel对象
 */
-(RegViewModel *)setRegbtnStyle:(RegViewController *)Vc;


/**
 提交注册资料
 
 @param Vc 当前视图控制器
 */
-(void)postRegdata:(RegViewController *)Vc;
@end
