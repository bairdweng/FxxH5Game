//
//  RegViewController.m
//  fxxproject
//
//  Created by  翁献山 on 2018/8/6.
//  Copyright © 2018年  翁献山. All rights reserved.
//

#import "RegViewController.h"
#import "RegViewModel.h"
@interface RegViewController ()
@property (strong,nonatomic) RegViewModel * ViewModel;
@end

@implementation RegViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    self.navigationItem.title=@"注册";
    [self.ViewModel setRegbtnStyle:self];
    // Do any additional setup after loading the view from its nib.
}
-(RegViewModel *)ViewModel{
    if (_ViewModel==nil) {
        _ViewModel =[[RegViewModel alloc]init];
    }
    return _ViewModel;
}
/**
 注册按钮事件

 @param sender 按钮事件
 */
- (IBAction)Regbtnsender:(UIButton *)sender {
    [self .ViewModel postRegdata:self];
}

- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

/*
#pragma mark - Navigation

// In a storyboard-based application, you will often want to do a little preparation before navigation
- (void)prepareForSegue:(UIStoryboardSegue *)segue sender:(id)sender {
    // Get the new view controller using [segue destinationViewController].
    // Pass the selected object to the new view controller.
}
*/

@end
