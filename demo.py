  # Make sure to activate alphapose env
  ''' conda activate alphapose '''
  
  # (Done) example images
  # python scripts/demo_inference.py --cfg configs/halpe_26/resnet/256x192_res50_lr1e-3_1x.yaml --checkpoint pretrained_models/halpe26_fast_res50_256x192.pth --indir examples/demo/ --save_img --showbox
  
  # (Done) openpose video
  # python scripts/demo_inference.py --cfg configs/halpe_26/resnet/256x192_res50_lr1e-3_1x.yaml --checkpoint pretrained_models/halpe26_fast_res50_256x192.pth --video /coc/pcba1/hkwon64/imuTube/repos_v2/pose/AlphaPose/examples/from_openpose/video.avi --outdir /coc/pcba1/hkwon64/imuTube/repos_v2/pose/AlphaPose/examples/from_openpose/res --save_video --showbox

  # (Done) openpose video + ReID tracking
  # python scripts/demo_inference.py --cfg configs/halpe_26/resnet/256x192_res50_lr1e-3_1x.yaml --checkpoint pretrained_models/halpe26_fast_res50_256x192.pth --video /coc/pcba1/hkwon64/imuTube/repos_v2/pose/AlphaPose/examples/from_openpose/video.avi --outdir /coc/pcba1/hkwon64/imuTube/repos_v2/pose/AlphaPose/examples/from_openpose/res_reID --pose_track --save_video --showbox

  # (Done) openpose video + ReID tracking [COCO]
  # CUDA_VISIBLE_DEVICES=1 python scripts/demo_inference.py --cfg configs/coco/resnet/256x192_res152_lr1e-3_1x-duc.yaml --checkpoint pretrained_models/fast_421_res152_256x192.pth --video /coc/pcba1/hkwon64/imuTube/repos_v2/pose/AlphaPose/examples/from_openpose/video.avi --outdir /coc/pcba1/hkwon64/imuTube/repos_v2/pose/AlphaPose/examples/from_openpose/res_reID_coco --pose_track --save_video --showbox


  # [O] (COCO) h36m + ReID tracking
  # CUDA_VISIBLE_DEVICES=1 python scripts/demo_inference.py --cfg configs/coco/resnet/256x192_res152_lr1e-3_1x-duc.yaml --checkpoint pretrained_models/fast_421_res152_256x192.pth --video /nethome/hkwon64/Datasets/public/human36m/S1/Videos/Walking.54138969.mp4 --outdir /coc/pcba1/hkwon64/imuTube/repos_v2/pose/AlphaPose/examples/h36m/coco --pose_track --save_video --showbox

  #-------------------------------------------------

  # [X] (136) h36m + ReID tracking: just so low performance ...
  # CUDA_VISIBLE_DEVICES=1 python scripts/demo_inference.py --cfg configs/halpe_136/256x192_res50_lr1e-3_2x-regression-coco_wholebody.yml --checkpoint pretrained_models/final_DPG.pth --video /nethome/hkwon64/Datasets/public/human36m/S1/Videos/Walking.54138969.mp4 --outdir /coc/pcba1/hkwon64/imuTube/repos_v2/pose/AlphaPose/examples/h36m/halpe_136 --pose_track --save_video --showbox

  # [X] (Fail) openpose video + MOT tracking : Takes tooo long or simply does not run. (looks like bug in the code)
  # python scripts/demo_inference.py --cfg configs/halpe_26/resnet/256x192_res50_lr1e-3_1x.yaml --checkpoint pretrained_models/halpe26_fast_res50_256x192.pth --video /coc/pcba1/hkwon64/imuTube/repos_v2/pose/AlphaPose/examples/from_openpose/video.avi --outdir /coc/pcba1/hkwon64/imuTube/repos_v2/pose/AlphaPose/examples/from_openpose/res_MOT --detector tracker --save_video --showbox

  # [X] (Done but ...) openpose video + Pose Flow tracking: Takes tooo long
  # python scripts/demo_inference.py --cfg configs/halpe_26/resnet/256x192_res50_lr1e-3_1x.yaml --checkpoint pretrained_models/halpe26_fast_res50_256x192.pth --video /coc/pcba1/hkwon64/imuTube/repos_v2/pose/AlphaPose/examples/from_openpose/video.avi --outdir /coc/pcba1/hkwon64/imuTube/repos_v2/pose/AlphaPose/examples/from_openpose/res_PoseFlow --pose_flow --save_video --showbox