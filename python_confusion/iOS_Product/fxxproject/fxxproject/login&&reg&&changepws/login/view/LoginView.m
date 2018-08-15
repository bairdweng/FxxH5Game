//
//  LoginView.m
//  fxxproject
//
//  Created by  翁献山 on 2018/8/6.
//  Copyright © 2018年  翁献山. All rights reserved.
//

#import "LoginView.h"

@implementation LoginView
-(void)awakeFromNib{
    [super awakeFromNib];
    self.loginview.layer.cornerRadius=5;
    self.loginbtn.layer.cornerRadius=5;
    self.loginbtn.layer.masksToBounds=YES;
   
}
-(void)changeloginviewheight:(BOOL )isshow{
    __weak typeof(self) weakself = self;
    [UIView animateWithDuration:0.8
                          delay:0.3
         usingSpringWithDamping:0.4
          initialSpringVelocity:7
                        options:UIViewAnimationOptionCurveLinear
                     animations:^{
                         weakself.loginviewLayoutConstraint.constant=isshow?0:500;
                         [weakself layoutIfNeeded];
                     } completion:^(BOOL finished) {
                         
                     }];
}
- (IBAction)btnsender:(UIButton *)sender {
    if (self.btnsenderblock) {
        self.btnsenderblock(sender.tag);
    }
}

/*
// Only override drawRect: if you perform custom drawing.
// An empty implementation adversely affects performance during animation.
- (void)drawRect:(CGRect)rect {
    // Drawing code
}
*/

@end
